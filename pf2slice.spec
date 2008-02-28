# please keep these three lines as they are used by the tagging script
# see build/module-tag.py for details
%define name pf2slice
%define version 1
%define taglevel 1

%define release %{taglevel}%{?pldistro:.%{pldistro}}%{?date:.%{date}}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	pf2slice - Tools for starting and managing the PF2 slice
Group:		Network/Monitoring
License:	GPL
Source0:	%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-buildroot
Provides:	pf2slice

%description
pf2slice - Populates the planetflow slice with the right initscript, keychains and so on

%prep
%setup -q

%install
rm -rf %{buildroot}
install -d -v %{buildroot}/etc/init.d
install -m 755 -v pf2slice-initscript %{buildroot}/etc/init.d/pf2slice
mkdir -p %{buildroot}/root/.ssh
cp authorized_keys %{buildroot}/root/.ssh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/init.d/pf2slice
/root/.ssh/authorized_keys

%post
chkconfig --add pf2slice
chkconfig pf2slice on

%changelog
