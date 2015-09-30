%global pypi_name oslo.messaging

Name:       python-oslo-messaging
Version:    XXX
Release:    XXX
Summary:    OpenStack common messaging library

License:    ASL 2.0
URL:        https://launchpad.net/oslo
Source0:    http://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-master.tar.gz

BuildArch:  noarch
Requires:   python-setuptools
Requires:   python-iso8601
Requires:   python-futurist
Requires:   python-oslo-config >= 1:1.9.3
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
Requires:   python-kombu
Requires:   python-qpid
Requires:   python-babel
Requires:   python-eventlet
Requires:   python-cachetools
Requires:   python-webob

BuildRequires: python2-devel
BuildRequires: python-setuptools
BuildRequires: python-pbr
BuildRequires: python-oslo-service
BuildRequires: python-cachetools
BuildRequires: python-futurist
BuildRequires: python-redis
BuildRequires: python-zmq


%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package doc
Summary:    Documentation for OpenStack common messaging library

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx >= 2.5.0

# for API autodoc
BuildRequires: python-iso8601
BuildRequires: python-oslo-config
BuildRequires: python-oslo-utils
BuildRequires: python-oslo-context
BuildRequires: python-oslo-serialization
BuildRequires: python-oslo-i18n
BuildRequires: python-six
BuildRequires: python-stevedore
BuildRequires: PyYAML
BuildRequires: python-babel
BuildRequires: python-fixtures
BuildRequires: python-kombu

%description doc
Documentation for the oslo.messaging library.

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

# let RPM handle deps
rm -rf {test-,}requirements.txt

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
%{python2_sitelib}/oslo_messaging
%{python2_sitelib}/*.egg-info
%{_bindir}/oslo-messaging-zmq-broker

%files doc
%license LICENSE
%doc doc/build/html

%changelog
