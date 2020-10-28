%define versiondate 20201028

Name:           syncany
Version:        0.4.9
Release:        %{versiondate}%{?dist}
Summary:        An open-source cloud storage and filesharing application

License:        GPLv3
URL:            https://www.syncany.org/

Source0:        %{name}-%{version}-%{versiondate}.zip

BuildArch: noarch

BuildRequires: java-devel

%description
Syncany allows users to securely backup and share certain folders of their
computers using any kind of storage. Syncany is open-source and provides data
encryption and incredible flexibility in terms of storage type and provider.

%prep
%setup -q -n %{name}-develop
./gradlew

%build
./gradlew installDist

%install
mkdir -p %{buildroot}%{_javadir}/syncany/bin
install -p -m 755 build/install/syncany/bin/sy %{buildroot}%{_javadir}/syncany/bin
install -p -m 755 build/install/syncany/bin/syncany %{buildroot}%{_javadir}/syncany/bin
mkdir -p %{buildroot}%{_javadir}/syncany/lib
install -p build/install/syncany/lib/* %{buildroot}%{_javadir}/syncany/lib

mkdir -p %{buildroot}%{_bindir}
ln -s ../..%{_javadir}/syncany/bin/sy %{buildroot}%{_bindir}/sy
ln -s ../..%{_javadir}/syncany/bin/syncany %{buildroot}%{_bindir}/syncany

%files
%{_bindir}/sy
%{_bindir}/syncany
%{_javadir}/syncany
%{_javadir}/syncany/bin/sy
%{_javadir}/syncany/bin/syncany
%{_javadir}/syncany/lib/syncany-develop.jar

%changelog
* Wed Oct 28 2020 Adrien Vergé <adrienverge@gmail.com> - 0.4.9-20201028
- Return to Gradle packaging (no precompiled package).
- Update to latest Git version (3fe40bb) to support Java 11.

* Mon Apr 30 2018 Adrien Vergé <adrienverge@gmail.com> - 0.4.9-1
- Update to latest upstream version.
- Use precompiled package from GitHub, because building on Fedora 28 fails.

* Fri Nov 27 2015 Adrien Vergé <adrienverge@gmail.com> - 0.4.7-1
- Update to latest upstream version.

* Thu Aug 27 2015 Adrien Vergé <adrienverge@gmail.com> - 0.4.6-4
- Return to old packaging style, including .jar dependencies and using the
  Gradle-generated bash script as entry point. Otherwise, Syncany plugin
  installation does not work.

* Thu Aug 27 2015 Adrien Vergé <adrienverge@gmail.com> - 0.4.6-3
- Downgrade dependency bouncycastle to 1.50 since the fix has been backported.

* Thu Aug 27 2015 Adrien Vergé <adrienverge@gmail.com> - 0.4.6-2
- Do not embed .jar dependencies and use %jpackage_script. This reduces the
  package size from 12 MB to 760 kB.

* Thu Aug 27 2015 Adrien Vergé <adrienverge@gmail.com> - 0.4.6-1
- First version.
