%define sonar_scanner_version 3.0.3.778
Name:       sonar-scanner
Version:    %{versionModule}
Release:    %{sonar_scanner_version}.%{releaseModule}
Summary:    An extendable open source continuous inspection
Group:      develenv
License:    http://creativecommons.org/licenses/by/3.0/
Packager:   softwaresano.com
URL:        https://www.sonarqube.org/
BuildArch:  x86_64
BuildRoot:  %{_topdir}/BUILDROOT
Requires:   jdk
AutoReqProv: no

Vendor:     softwaresano

%define package_name sonar-scanner
%define target_dir /
%define sonar_home /opt/ss/develenv/platform/sonar-scanner

%description
Sonar is the central place to manage code quality, offering visual reporting on
and across projects and enabling to replay the past to follow metrics evolution

# ------------------------------------------------------------------------------
# CLEAN
# ------------------------------------------------------------------------------
%clean
rm -rf $RPM_BUILD_ROOT

# ------------------------------------------------------------------------------
# INSTALL
# ------------------------------------------------------------------------------
%install
%{__mkdir_p} $RPM_BUILD_ROOT/%{sonar_home}  $RPM_BUILD_ROOT/usr/bin/
cd $RPM_BUILD_ROOT/%{sonar_home}
curl -L -O -L https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-%{sonar_scanner_version}-linux.zip

unzip sonar-scanner-cli-%{sonar_scanner_version}-linux.zip
rm -f sonar-scanner-cli-%{sonar_scanner_version}-linux.zip
mv sonar-scanner-cli-%{sonar_scanner_version}-linux/* .
rm -rf sonar-scanner-cli-%{sonar_scanner_version}-linux/
rm -rf jre
sed -i s:^use_embedded_jre=true:use_embedded_jre=false:g bin/sonar-scanner
ln -sf %{sonar_home}/bin/sonar-scanner ${RPM_BUILD_ROOT}/usr/bin/sonar-scanner

# ------------------------------------------------------------------------------
# PRE-INSTALL
# ------------------------------------------------------------------------------
%pre
# ------------------------------------------------------------------------------
# POST-INSTALL
# ------------------------------------------------------------------------------
%post
# ------------------------------------------------------------------------------
# PRE-UNINSTALL
# ------------------------------------------------------------------------------
%preun
# ------------------------------------------------------------------------------
# POST-UNINSTALL
# ------------------------------------------------------------------------------
%postun
%files
%defattr(-,root,root,-)
/usr/bin/*
%config(noreplace) %{sonar_home}/conf/*
%{sonar_home}/bin/*
%{sonar_home}/lib/*
%doc ../../../../README.md