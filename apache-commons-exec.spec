Name:           apache-commons-exec
Version:        1.3
Release:        10
Summary:        A library to reliably execute external processes from within the JVM
License:        ASL 2.0
URL:            http://commons.apache.org/exec/
Source0:        http://www.apache.org/dist/commons/exec/source/commons-exec-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local mvn(junit:junit) mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin) iputils

%description
The apache-commons-exec package contains a library to reliably
execute external processes from within the JVM.

%package help
Summary:        Documents for apache-commons-exec

Provides:       %{name}-javadoc = %{version}-%{release}
Obsoletes:      %{name}-javadoc < %{version}-%{release}

%description help
The apache-commons-exec-help package contains related documents.

%prep
%autosetup -n commons-exec-%{version}-src -p1

find src/test/scripts -name "*.sh" | xargs chmod a+x
find ./ -name Exec57Test.java | xargs rm

%mvn_file :commons-exec commons-exec %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt STATUS RELEASE-NOTES.txt

%files help -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Mar 11 2020 Jiangping Hu <hujp1985@foxmail.com> - 1.3-10
- Package init
