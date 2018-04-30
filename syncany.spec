Name:           syncany
Version:        0.4.7
Release:        1%{?dist}
Summary:        An open-source cloud storage and filesharing application

License:        GPLv3
URL:            https://www.syncany.org/

Source0:        %{name}-%{version}-alpha.tar.gz
                # https://github.com/syncany/syncany/archive/v0.4.7-alpha.tar.gz

BuildArch: noarch

BuildRequires: java-devel
BuildRequires: gradle
#BuildRequires: xmvn-subst

Requires: java-headless
Requires: apache-commons-io >= 2.4
Requires: bouncycastle >= 1.50
Requires: simple-xml >= 2.7.1
Requires: guava >= 15.0
Requires: apache-commons-codec >= 1.8
Requires: hsqldb >= 2.3.1
Requires: jsemver >= 0.7.2
Requires: undertow >= 1.1.0
Requires: jpathwatch >= 0.95
Requires: httpcomponents-client >= 4.3.4
Requires: google-gson >= 2.2.4
Requires: jopt-simple >= 4.5

%description
Syncany allows users to securely backup and share certain folders of their
computers using any kind of storage. Syncany is open-source and provides data
encryption and incredible flexibility in terms of storage type and provider.

%prep
%setup -q -n %{name}-%{version}-alpha

%build
gradle installApp
#xmvn-subst build/install/syncany/lib

%install
mkdir -p %{buildroot}%{_javadir}/syncany/bin
install -p -m 755 build/install/syncany/bin/sy %{buildroot}%{_javadir}/syncany/bin
install -p -m 755 build/install/syncany/bin/syncany %{buildroot}%{_javadir}/syncany/bin
mkdir -p %{buildroot}%{_javadir}/syncany/lib
install -p build/install/syncany/lib/* %{buildroot}%{_javadir}/syncany/lib

mkdir -p %{buildroot}%{_bindir}
ln -s ../..%{_javadir}/syncany/bin/sy %{buildroot}%{_bindir}/sy
ln -s ../..%{_javadir}/syncany/bin/syncany %{buildroot}%{_bindir}/syncany

#mkdir -p %{buildroot}%{_javadir}
#install -p -D build/install/syncany/lib/syncany-0.4.6-alpha.jar %{buildroot}%{_javadir}/syncany.jar
#install -p -D build/install/syncany/lib/syncany-cli-0.4.6-alpha*.jar %{buildroot}%{_javadir}/syncany-cli.jar
#install -p -D build/install/syncany/lib/syncany-lib-0.4.6-alpha*.jar %{buildroot}%{_javadir}/syncany-lib.jar
#install -p -D build/install/syncany/lib/syncany-util-0.4.6-alpha*.jar %{buildroot}%{_javadir}/syncany-util.jar
#
#%jpackage_script org.syncany.Syncany "" "" commons-codec:commons-io:commons-logging:guava:httpcomponents/httpclient:httpcomponents/httpcore:jsemver/java-semver:jboss-annotations-1.2-api/jboss-annotations-api_1.2_spec:jboss-logging/jboss-logging:jboss-servlet-3.1-api/jboss-servlet-api_3.1_spec:jopt-simple/jopt-simple:simple-xml:undertow/undertow-core:undertow/undertow-servlet:undertow/undertow-websockets-jsr:xnio/xnio-api:xnio/xnio-nio:syncany:syncany-cli:syncany-lib:syncany-util syncany true
#ln -s syncany %{buildroot}%{_bindir}/sy

%files
%{_bindir}/sy
%{_bindir}/syncany
%{_javadir}/syncany
%{_javadir}/syncany/bin/sy
%{_javadir}/syncany/bin/syncany
%{_javadir}/syncany/lib/syncany-%{version}-alpha.jar
# others...

#%{_javadir}/syncany.jar
#%{_javadir}/syncany-cli.jar
#%{_javadir}/syncany-lib.jar
#%{_javadir}/syncany-util.jar

%changelog
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
