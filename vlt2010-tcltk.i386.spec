# Generated from:
#  /vlt/VLT2010/tcltk
#
# Pre-Installation:
#  cd 
#  vi .rpmmacros
#     %_topdir /home/vltmgr/RPMBUILD
#     %_home /home/vltmgr
#
# Creation of the RPM:
#  cd ~/RPMBUILD/SOURCES
#  tar cvzf vlt2010-tcltk-0.1.i386.tar.gz -C / vlt/VLT2010/tcltk
#  cd ~/RPMBUILD/SPECS
#  rpmbuild -bb vlt2010-tcltk.i386.spec
#
# Installation of the RPM
# As root:
#  mv /vlt/VLT2010/tcltk /vlt/VLT2010/tcltk.old
#  rpm -ihv /home/vltmgr/RPMBUILD/RPMS/i386/vlt2010-tcltk-0.1-1.i386.rpm

Name: vlt2010-tcltk
Summary: VLT2010 tcltk binary
Version: 0.1
Release: 4
Group: Applications/ESO/VLT2010
License: ESO
BuildRoot: %{_home}/RPMBUILD/BUILD/%{name}-%{version}-%{release}
BuildArch: i386
Source: %{name}-%{version}.i386.tar.gz
Provides: VLT2010/tcltk
# Do not generate dependencies otherwise SNMP will complain at installation
AutoReqProv: no

%define __os_install_post %{nil}

%description
VLT2010: tcltk
Compiled on SL53
vlt2010-tcltk generated on 2009-10-13

%changelog
* Wed Jul 28 2009 VLT2010 tcltk Beta 0.1
- First integration with SL53

%prep
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT
tar xzf $RPM_SOURCE_DIR/%{name}-%{version}.i386.tar.gz

%build

%install

%files

%defattr (755, vltmgr, vlt)
/vlt/VLT2010/tcltk

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
