%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

%global _docdir_fmt %{name}
%global srcname ddt

Name:           python-%{srcname}
Version:        1.1.1
Release:        3%{?dist}
Summary:        Python library to multiply test cases

License:        MIT
URL:            https://github.com/txels/ddt
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
DDT (Data-Driven Tests) allows you to multiply one test case by running it with\
different test data, and make it appear as multiple test cases. It is used in\
combination with other testing frameworks like unittest and nose.

%description %{_description}

%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-mock
BuildRequires:  python-six >= 1.4.0
BuildRequires:  PyYAML
%else
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
BuildRequires:  python2-mock
BuildRequires:  python2-six >= 1.4.0
BuildRequires:  python2-yaml
%endif
%if ! 0%{?rhel} || 0%{?rhel} > 7
Recommends:     python2-yaml
%endif

%description -n python2-%{srcname} %{_description}

Python 2 version.

%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-six >= 1.4.0
BuildRequires:  python3-yaml
%if ! 0%{?rhel} || 0%{?rhel} > 7
Recommends:     python3-yaml
%endif

%description -n python3-%{srcname} %{_description}

Python 3 version.
%endif

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%py2_install
%if %{with python3}
%py3_install
%endif

%check
nosetests-%{python2_version} -v
%if %{with python3}
nosetests-%{python3_version} -v
%endif

%files -n python2-%{srcname}
%license LICENSE.md
%doc README.md
%{python2_sitelib}/%{srcname}-*.egg-info
%{python2_sitelib}/%{srcname}.py*

%if %{with python3}
%files -n python3-%{srcname}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}.py
%{python3_sitelib}/__pycache__/%{srcname}.*
%endif

%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.1-2
- Add EPEL7 conditionals

* Wed Dec 28 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.1-1
- Update to 1.1.1
- Modernize spec

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 20 2016 Carl George <carl.george@rackspace.com> - 1.0.2-1
- Latest upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Carl George <carl.george@rackspace.com> - 1.0.1-2
- Remove coverage build dependency
- Change python3 control macros to a bcond macro
- Add bcond macro to optionally require explicit python2 names

* Thu Nov 19 2015 Carl George <carl.george@rackspace.com> - 1.0.1-1
- Latest upstream

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Sep 01 2015 Carl George <carl.george@rackspace.com> - 1.0.0-3
- Update to new packaging guidelines

* Mon Jul 20 2015 Carl George <carl.george@rackspace.com> - 1.0.0-2
- Remove separate py3 build directory
- Update summary and description
- Use a common license and documentation directories between PY2/3 packages

* Thu Jul 16 2015 Carl George <carl.george@rackspace.com> - 1.0.0-1
- Initial spec file
