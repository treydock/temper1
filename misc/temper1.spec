%global commit 722991add4a6a239271e1f029ebe4daaad719496
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global build_date %(date +%Y%m%d)
%global group_name temper

Name:           temper1
Version:        %{build_date}git%{shortcommit}
Release:        1%{?dist}
Summary:        Enhanced utility for TEMPer1 USB temperature probes on Linux

Group:          System Environment/Base
License:        GPLv2+
URL:            https://github.com/ssllab/temper1
Source0:        https://github.com/ssllab/temper1/archive/%{commit}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libusb-devel
Requires:       libusb
Requires:       udev
Requires(pre):  shadow-utils
Requires(postun): shadow-utils


%description
Enhanced utility for TEMPer1 USB temperature probes on Linux

%prep
%setup -qn %{name}-%{commit}


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_prefix}/local/bin
mkdir -p %{buildroot}%{_sysconfdir}/temper
mkdir -p %{buildroot}/lib/udev/rules.d

install -m 0755 temper1 %{buildroot}%{_bindir}/temper1
install -m 0755 get_temps.sh %{buildroot}%{_prefix}/local/bin/get_temps.sh
install -m 0644 temper1.conf.sample %{buildroot}%{_sysconfdir}/temper/temper1.conf
install -m 0644 60-temper.rules %{buildroot}/lib/udev/rules.d/60-temper.rules


%clean
rm -rf %{buildroot}


%post
/sbin/udevadm trigger


%postun
groupdel %{group_name} >/dev/null


%pre
getent group %{group_name} >/dev/null || groupadd -r %{group_name}


%files
%defattr(-,root,root,-)
%attr(755, -, -) %{_bindir}/temper1
%attr(755, -, -) %{_prefix}/local/bin/get_temps.sh
%config %{_sysconfdir}/temper/temper1.conf
/lib/udev/rules.d/60-temper.rules


%changelog
* Wed Apr 10 2013 Trey Dockendorf <treydock@gmail.com> - 20130410git722991a-1
- Initial SPEC file creation

