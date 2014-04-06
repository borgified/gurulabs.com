# Generated from:
#  /vlt/VLT2010/midas
#
# Pre-Installation:
#  cd 
#  vi .rpmmacros
#     %_topdir /home/vltmgr/RPMBUILD
#     %_home /home/vltmgr
#
# Creation of the RPM:
#  cd ~/RPMBUILD/SOURCES
#  tar cvzf vlt2010-midas-0.1.i386.tar.gz -C / vlt/VLT2010/midas
#  cd ~/RPMBUILD/SPECS
#  rpmbuild -bb vlt2010-midas.i386.spec
#
# Installation of the RPM
# As root:
#  mv /vlt/VLT2010/midas /vlt/VLT2010/midas.old
#  rpm -ihv /home/vltmgr/RPMBUILD/RPMS/i386/vlt2010-midas-0.1-1.i386.rpm

Name: vlt2010-midas
Summary: VLT2010 midas binary
Version: 0.1
Release: 7
Group: Applications/ESO/VLT2010
License: ESO
BuildRoot: %{_home}/RPMBUILD/BUILD/%{name}-%{version}-%{release}
BuildArch: i386
Source: %{name}-%{version}.i386.tar.gz
Provides: VLT2010/midas
# Do not generate dependencies otherwise SNMP will complain at installation
AutoReqProv: no

%description
VLT2010: midas
Compiled on SL53
vlt2010-midas generated on 2010-02-01
%changelog
* Wed Jul 28 2009 VLT2010 midas Beta 0.1
- First integration with SL53

%define __os_install_post %{nil}

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
tar xzf $RPM_SOURCE_DIR/%{name}-%{version}.i386.tar.gz

%build

%install

%files

%defattr (755, vltmgr, vlt)
/vlt/VLT2010/midas

%clean
rm -fr $RPM_BUILD_ROOT/*

%post
if ! grep vlt /etc/group >/dev/null 2>&1 ; then
  groupadd -g 300 vlt
fi

if ! id vltmgr >/dev/null 2>&1 ; then
  useradd -M -u 450 -g 300 vltmgr
fi

ldconfig
