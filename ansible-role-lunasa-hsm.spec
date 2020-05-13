# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility

%global srcname ansible_role_lunasa_hsm
%global rolename ansible-role-lunasa-hsm

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:          %{rolename}
Version:       0.1.0
Release:       1%{?dist}
Summary:       Ansible role for configuring Luna Network HSM

Group:         System Environment/Base
License:       ASL 2.0
URL:           https://opendev.org/openstack/ansible-role-lunasa-hsm
Source0:       https://github.com/dmend/%{rolename}/archive/%{upstream_version}.tar.gz

BuildArch:     noarch
BuildRequires: git
BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-pbr

# Handle python2 exception
%if %{pyver} == 2
Requires:      ansible
%else
Requires:      python3dist(ansible)
%endif

%description

Ansible role to configure Luna Network HSM clients

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git

%build
%{pyver_build}

%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1
%{pyver_install}

%files
%doc README.rst
%license LICENSE
%{pyver_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/

%changelog
* Wed Jun 10 2020 Douglas Mendizábal <dmendiza@redhat.com> - 0.1.0-1
- Update to 0.1.0

