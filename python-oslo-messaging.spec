%global pypi_name oslo.messaging

Name:       python-oslo-messaging
Version:    1.8.1
Release:    1%{?dist}
Summary:    OpenStack common messaging library

Group:      Development/Languages
License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    https://pypi.python.org/packages/source/o/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:  noarch
Requires:   python-setuptools
Requires:   python-iso8601
Requires:   python-oslo-config >= 1:1.9.3
Requires:   python-oslo-context
Requires:   python-oslo-utils
Requires:   python-oslo-serialization
Requires:   python-oslo-i18n
Requires:   python-oslo-middleware
Requires:   python-six >= 1.9.0
Requires:   python-stevedore
Requires:   PyYAML
Requires:   python-kombu
Requires:   python-qpid
Requires:   python-babel
Requires:   python-eventlet

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package doc
Summary:    Documentation for OpenStack common messaging library
Group:      Documentation

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx >= 2.5.0

# for API autodoc
BuildRequires: python-iso8601
BuildRequires: python-oslo-config
BuildRequires: python-oslo-utils
BuildRequires: python-oslo-serialization
BuildRequires: python-oslo-i18n
BuildRequires: python-six
BuildRequires: python-stevedore
BuildRequires: PyYAML
BuildRequires: python-babel

%description doc
Documentation for the oslo.messaging library.

%prep
%setup -q -n %{pypi_name}-%{version}

# let RPM handle deps
rm -rf requirements.txt

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

# Delete tests
rm -fr %{buildroot}%{python_sitelib}/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%check

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo
%{python2_sitelib}/oslo_messaging
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*-nspkg.pth
%{_bindir}/oslo-messaging-zmq-receiver

%files doc
%license LICENSE
%doc doc/build/html

%changelog
* Wed Apr 08 2015 Alan Pevec <alan.pevec@redhat.com> 1.8.1-1
- Update to upstream 1.8.1

* Thu Jan 08 2015 Alan Pevec <apevec@redhat.com> - 1.4.1-3
- Fix reconnect exception handler (Dan Smith) rhbz#1175685

* Tue Dec 02 2014 Alan Pevec <apevec@redhat.com> - 1.4.1-2
- AMQP 1.0 driver fixes (Ken Giusti) LP#1392868 LP#1385445

* Sun Sep 21 2014 Alan Pevec <apevec@redhat.com> - 1.4.0.0-4
- Final release 1.4.0

* Wed Sep 17 2014 Alan Pevec <apevec@redhat.com> - 1.4.0.0-3.a5
- Latest upstream

* Wed Jul 09 2014 Pádraig Brady <pbrady@redhat.com> - 1.4.0.0-1
- Latest upstream

* Tue Jun 10 2014 Pádraig Brady <pbrady@redhat.com> - 1.3.0.2-4
- Fix message routing with newer QPID #1103800

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Pádraig Brady <pbrady@redhat.com> - 1.3.0.2-2
- Update python-six dependency to >= 1.6 to support Icehouse

* Thu Apr 24 2014 Pádraig Brady <pbrady@redhat.com> - 1.3.0.2-1
- Update to icehouse stable release
- Add dependency on newer python-eventlet

* Fri Apr 11 2014 Pádraig Brady <pbrady@redhat.com> - 1.3.0-0.2.a9
- Add dependencies on python-kombu, python-qpid, and PyYAML

* Tue Mar 18 2014 Pádraig Brady <pbrady@redhat.com> - 1.3.0-0.1.a9
- Latest upstream

* Tue Feb 11 2014 Pádraig Brady <pbrady@redhat.com> - 1.3.0-0.1.a7
- Update to 1.3.0a7.

* Thu Jan  2 2014 Pádraig Brady <pbrady@redhat.com> - 1.3.0-0.1.a2
- Update to 1.3.0a2.

* Tue Sep  3 2013 Mark McLoughlin <markmc@redhat.com> - 1.2.0-0.1.a11
- Update to a11 development snapshot.

* Mon Aug 12 2013 Mark McLoughlin <markmc@redhat.com> - 1.2.0-0.1.a2
- Initial package.
