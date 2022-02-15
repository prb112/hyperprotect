Name:		keyprotect-luks
Version:	1.0
Release:	1%{?dist}
Summary:	IBM HPCS Key Protect Integration with LUKS
BuildArch:	noarch

Group:		None
License:	Apache 2.0
URL:		https://example.com
Source0:	%{name}-%{version}.tar.gz

#BuildRequires:
Requires:	python3

%description
%{name} provides integration between IBM HPCS Key Protect
and LUKS via the kernel keyring.

%global BUILD_AND_PACKAGE_DRACUT 0

%prep
%setup -q


%install
%if "%{BUILD_AND_PACKAGE_DRACUT}" == "1"
make install install-dracut DESTDIR=%{buildroot}
%else
make install DESTDIR=%{buildroot}
%endif


%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0644,root,root) %{_prefix}/lib/systemd/system/%{name}.service
%attr(0644,root,root) %{_sharedstatedir}/%{name}/logon
%attr(0644,root,root) %{_sharedstatedir}/%{name}/user
%attr(0644,root,root) %{_docdir}/%{name}/%{name}.ini
%attr(0644,root,root) %{_mandir}/man1/%{name}.1.gz
%if "%{BUILD_AND_PACKAGE_DRACUT}" == "1"
%attr(0755,root,root) %{_prefix}/lib/dracut/modules.d/85%{name}/%{name}.sh
%attr(0755,root,root) %{_prefix}/lib/dracut/modules.d/85%{name}/module-setup.sh
%attr(0644,root,root) %{_sysconfdir}/dracut.conf.d/%{name}.conf
%attr(0755,root,root) %{_prefix}/lib/dracut/modules.d/83tss/module-setup.sh
%attr(0755,root,root) %{_prefix}/lib/dracut/modules.d/83tss/start-tcsd.sh
%attr(0755,root,root) %{_prefix}/lib/dracut/modules.d/83tss/stop-tcsd.sh
%attr(0644,root,root) %{_sysconfdir}/dracut.conf.d/tss.conf
%endif

%changelog
* Thu Jan 13 2022 George Wilson <gcwilson@linux.ibm.com>
- Add BUILD_AND_PACKAGE_DRACUT conditional
* Fri Jun 18 2021 George Wilson <gcwilson@linux.ibm.com>
- Add tss dracut module
* Wed Jun 16 2021 George Wilson <gcwilson@linux.ibm.com>
- Add dracutl module skeleton
* Mon May 17 2021 George Wilson <gcwilson@linux.ibm.com>
- Add key dirs and keyprotect.ini
* Thu May 06 2021 George Wilson <gcwilson@linux.ibm.com>
- Inital packaging

