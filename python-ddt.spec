%if 0%{?rhel} && 0%{?rhel} <= 6
%global __python2 %{_bindir}/python2
%global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python2_version %(%{__python2} -c "import sys; sys.stdout.write(sys.version[:3])")
%endif

%if 0%{?fedora}
%global with_python3 1
%global _docdir_fmt %{name}
%endif

%global srcname ddt

Name: python-%{srcname}
Version: 1.0.1
Release: 1%{?dist}
Summary: A Python library to multiply test cases
Group: Development/Libraries
License: MIT
URL: https://github.com/txels/%{srcname}
Source0: https://github.com/txels/%{srcname}/archive/%{version}.tar.gz

BuildArch: noarch
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python3-devel
BuildRequires: python3-setuptools


%description
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.


%package -n python2-%{srcname}
Summary: Data-Driven/Decorated Tests
BuildRequires: python2-coverage
BuildRequires: python2-nose
BuildRequires: python2-six >= 1.4.0
%{?python_provide:%python_provide python2-%{srcname}}


%description -n python2-%{srcname}
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.


%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary: Data-Driven/Decorated Tests
BuildRequires: python3-coverage
BuildRequires: python3-nose
BuildRequires: python3-six >= 1.4.0
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.
%endif # with_python3


%prep
%setup -q -n %{srcname}-%{version}


%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif # with_python3


%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif # with_python3


%check
nosetests-%{python2_version} --nocapture --with-coverage --cover-package=ddt --cover-html
%if 0%{?with_python3}
nosetests-%{python3_version} --nocapture --with-coverage --cover-package=ddt --cover-html
%endif # with_python3


%files -n python2-%{srcname}
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md
%{python2_sitelib}/%{srcname}*


%if 0%{?with_python3}
%files -n python3-%{srcname}
%{!?_licensedir:%global license %%doc}
%license LICENSE.md
%doc README.md
%{python3_sitelib}/%{srcname}*
%{python3_sitelib}/__pycache__/%{srcname}*
%endif # with_python3


%changelog
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
