%if 0%{?fedora} >= 24
%global with_python3 1
%endif

%global pypi_name oslo.messaging
%global pkg_name oslo-messaging

Name:       python-oslo-messaging
Version:    XXX
Release:    XXX
Summary:    OpenStack common messaging library

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    http://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-master.tar.gz
BuildArch:  noarch

BuildRequires: git

%package -n python2-%{pkg_name}
Summary:    OpenStack common messaging library
%{?python_provide:%python_provide python2-%{pkg_name}}

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-cachetools
BuildRequires: python-futurist
BuildRequires: python-redis
BuildRequires: python-zmq
# Required for tests
BuildRequires: python-fixtures
BuildRequires: python-hacking
BuildRequires: python-kafka
BuildRequires: python-kombu >= 3.0.7
BuildRequires: python-mock
BuildRequires: python-mox3
BuildRequires: python-oslo-config
BuildRequires: python-oslo-context
BuildRequires: python-oslo-middleware
BuildRequires: python-oslo-serialization
BuildRequires: python-oslo-service
BuildRequires: python-oslo-utils
BuildRequires: python-oslotest
BuildRequires: python-subunit
BuildRequires: python-testrepository
BuildRequires: python-testscenarios
BuildRequires: python-testtools

Requires:   python-setuptools
Requires:   python-iso8601
Requires:   python-futurist >= 0.1.2
Requires:   python-oslo-config >= 2:2.3.0
Requires:   python-oslo-context
Requires:   python-oslo-utils
Requires:   python-oslo-serialization
Requires:   python-oslo-service
Requires:   python-oslo-i18n
Requires:   python-oslo-log
Requires:   python-oslo-middleware
Requires:   python-six >= 1.9.0
Requires:   python-stevedore
Requires:   PyYAML
Requires:   python-kombu >= 3.0.7
Requires:   python-babel
Requires:   python-eventlet
Requires:   python-cachetools
Requires:   python-webob

%description -n python2-%{pkg_name}
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package -n python-%{pkg_name}-doc
Summary:    Documentation for OpenStack common messaging library

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx >= 2.5.0

# for API autodoc
BuildRequires: python-iso8601
BuildRequires: python-oslo-config
BuildRequires: python-oslo-context
BuildRequires: python-oslo-i18n
BuildRequires: python-oslo-middleware
BuildRequires: python-oslo-serialization
BuildRequires: python-oslo-service
BuildRequires: python-oslo-utils
BuildRequires: python-six
BuildRequires: python-stevedore
BuildRequires: PyYAML
BuildRequires: python-babel
BuildRequires: python-fixtures
BuildRequires: python-kombu >= 3.0.7


%description -n python-%{pkg_name}-doc
Documentation for the oslo.messaging library.

%package -n python2-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python-%{pkg_name} = %{version}-%{release}
Requires:      python-kafka
Requires:      python-oslo-config
Requires:      python-oslo-context
Requires:      python-oslo-middleware
Requires:      python-oslo-serialization
Requires:      python-oslo-service
Requires:      python-oslo-utils
Requires:      python-oslotest
Requires:      python-testrepository
Requires:      python-testscenarios
Requires:      python-testtools

%description -n python2-%{pkg_name}-tests
Tests for the OpenStack common messaging library.

%if 0%{?with_python3}
%package -n python3-%{pkg_name}
Summary:    OpenStack common messaging library
%{?python_provide:%python_provide python3-%{pkg_name}}

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr
BuildRequires: python3-cachetools
BuildRequires: python3-futurist
BuildRequires: python3-redis
BuildRequires: python3-zmq

# Required for tests
BuildRequires: python3-kafka
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-context
BuildRequires: python3-oslo-middleware
BuildRequires: python3-oslo-serialization
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslotest
BuildRequires: python3-testrepository
BuildRequires: python3-testscenarios
BuildRequires: python3-testtools

Requires:   python3-setuptools
Requires:   python3-iso8601
Requires:   python3-futurist >= 0.1.2
Requires:   python3-oslo-config >= 2:2.3.0
Requires:   python3-oslo-context
Requires:   python3-oslo-utils
Requires:   python3-oslo-serialization
Requires:   python3-oslo-service
Requires:   python3-oslo-i18n
Requires:   python3-oslo-log
Requires:   python3-oslo-middleware
Requires:   python3-six >= 1.9.0
Requires:   python3-stevedore
Requires:   python3-PyYAML
Requires:   python3-kombu >= 3.0.7
Requires:   python3-babel
Requires:   python3-eventlet
Requires:   python3-cachetools
Requires:   python3-webob

%description -n python3-%{pkg_name}
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package -n python3-%{pkg_name}-tests
Summary:    Tests for OpenStack common messaging library

Requires:      python3-%{pkg_name} = %{version}-%{release}
Requires:      python3-kafka
Requires:      python3-oslo-config
Requires:      python3-oslo-context
Requires:      python3-oslo-middleware
Requires:      python3-oslo-serialization
Requires:      python3-oslo-service
Requires:      python3-oslo-utils
Requires:      python3-oslotest
Requires:      python3-testrepository
Requires:      python3-testscenarios
Requires:      python3-testtools

%description -n python3-%{pkg_name}-tests
Tests for the OpenStack common messaging library.
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

%prep
# FIXME: workaround required to build
%autosetup -n %{pypi_name}-%{upstream_version} -S git

# let RPM handle deps
rm -rf {test-,}requirements.txt

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python3}
%py3_install
%endif
%py2_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%check
# Temporarily disabling tests until we have
# mock >= 1.2 and pika_pool
%{__python2} setup.py test ||
%if 0%{?with_python3}
rm -rf .testrepository
%{__python3} setup.py test ||
%endif

%files -n python2-%{pkg_name}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_messaging
%{python2_sitelib}/*.egg-info
%{_bindir}/oslo-messaging-zmq-broker
%exclude %{python2_sitelib}/oslo_messaging/tests

%files -n python-%{pkg_name}-doc
%license LICENSE
%doc doc/build/html

%files -n python2-%{pkg_name}-tests
%{python2_sitelib}/oslo_messaging/tests

%if 0%{?with_python3}
%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_messaging
%{python3_sitelib}/*.egg-info
%exclude %{python3_sitelib}/oslo_messaging/tests

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_messaging/tests
%endif

%changelog
