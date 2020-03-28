Name:           eldaw-release
Version:        8
Release:        1%{dist}
Summary:        Enterprise Linux Digital Audio Workstation repository configuration

Group:          System Environment/Base
License:        GPLv2

URL:            https://teknik.tv/projects/eldaw
Source0:        https://download.teknik.tv/pub/eldaw/RPM-GPG-KEY-ELDAW-8
Source1:        README
Source2:        LICENSE
Source3:        eldaw.repo
Source4:        eldaw-testing.repo

BuildArch:      noarch
Requires:       redhat-release >=  %{version}
Requires:       epel-release >=  %{version}
Conflicts:      fedora-release

%description
This package contains the Enterprise Linux Digital Audio Workstation packages (ELDAW) repository
GPG key as well as configuration for dnf.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
install -pm 644 %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT

install -Dpm 644 %{SOURCE0} \
 $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ELDAW-%{version}

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE3} %{SOURCE4} \
 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%files
%doc README
%license LICENSE
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/*

%changelog
* Sat Mar 28 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 8-1
- Initial build
