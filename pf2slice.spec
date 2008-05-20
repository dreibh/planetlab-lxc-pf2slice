# please keep these three lines as they are used by the tagging script
# see build/module-tag.py for details
%define name pf2slice
%define version 1.0
%define taglevel 2

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
install -d -m 700 %{buildroot}/home/pl_netflow/.ssh
install -m 600 authorized_keys %{buildroot}/home/pl_netflow/.ssh/authorized_keys
mkdir -p %{buildroot}/home/pl_netflow/.ssh
mkdir -p %{buildroot}/pf


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/etc/init.d/pf2slice
/home/pl_netflow/.ssh/authorized_keys
/home/*
/pf

%post
chkconfig --add pf2slice
chkconfig pf2slice on

%changelog
* Tue May 20 2008 Faiyaz Ahmed <faiyaza@cs.princeton.edu> - pf2slice-1.0-2
- 
- The PlanetFlow slice needs to mount the netflow logs from the root context.  The initscript will now attempt to trigger vsys to mount the logs repeatedly until vsys responds.  
- 

