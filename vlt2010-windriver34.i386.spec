# Generated from:
#  /vlt/VLT2010/WindRiver-3.4
#
# Pre-Installation:
#  cd 
#  vi .rpmmacros
#     %_topdir /home/vltmgr/RPMBUILD
#     %_home /home/vltmgr
#
# Creation of the RPM:
#  cd ~/RPMBUILD/SOURCES
#  tar cvzf vlt2010-windriver34-0.1.i386.tar.gz -C / vlt/VLT2010/WindRiver-3.4
#  cd ~/RPMBUILD/SPECS
#  rpmbuild -bb vlt2010-windriver34.i386.spec
#
# Installation of the RPM
# As root:
#  mv /vlt/VLT2010/WindRiver-3.4 /vlt/VLT2010/WindRiver-3.4.old
#  rpm -ihv /home/vltmgr/RPMBUILD/RPMS/i386/vlt2010-windriver34-0.1-1.i386.rpm

Name: vlt2010-windriver34
Summary: VLT2010 WindRiver-3.4 binary
Version: 0.1
Release: 8
Group: Applications/ESO/VLT2010
License: ESO
BuildRoot: %{_home}/RPMBUILD/BUILD/%{name}-%{version}-%{release}
BuildArch: i386
Source: %{name}-%{version}.i386.tar.gz
Provides: VLT2010/WindRiver-3.4
# Do not generate dependencies otherwise SNMP will complain at installation
AutoReqProv: no
#Requires: 

%define __os_install_post %{nil} 

%description
VLT2010: WindRiver-3.4
Compiled on SL53
vlt2010-windriver34 generated on 2009-10-29

%changelog
* Wed Jul 28 2009 VLT2010 WindRiver-3.4 Beta 0.1
- First integration with SL53

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
tar xzf $RPM_SOURCE_DIR/%{name}-%{version}.i386.tar.gz
cd vlt/VLT2010
#ln -s  WindRiver-3.4/vxworks-6.4 vw6.4
%build

%install

%files
#/vlt/VLT2010/vw6.4

%defattr (755, vltmgr, vlt)
/vlt/VLT2010/WindRiver-3.4

%defattr (777, vltmgr, vlt)
#/vlt/VLT2010/WindRiver-3.4/.wind

%clean
find $RPM_BUILD_ROOT -type d -exec chmod +rwx {} \; 
rm -fr $RPM_BUILD_ROOT/*

%post
if ! grep vlt /etc/group >/dev/null 2>&1 ; then
  groupadd -g 300 vlt
fi

if ! id vltmgr >/dev/null 2>&1 ; then
  useradd -M -u 450 -g 300 vltmgr
fi

ldconfig
