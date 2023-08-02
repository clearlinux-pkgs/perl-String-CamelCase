#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-CamelCase
Version  : 0.04
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/H/HI/HIO/String-CamelCase-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HI/HIO/String-CamelCase-0.04.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-camelcase-perl/libstring-camelcase-perl_0.04-1.debian.tar.xz
Summary  : 'camelcase, de-camelcase'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-String-CamelCase-license = %{version}-%{release}
Requires: perl-String-CamelCase-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
String-CamelCase
INSTALLATION
To install this module, run the following commands:

%package dev
Summary: dev components for the perl-String-CamelCase package.
Group: Development
Provides: perl-String-CamelCase-devel = %{version}-%{release}
Requires: perl-String-CamelCase = %{version}-%{release}

%description dev
dev components for the perl-String-CamelCase package.


%package license
Summary: license components for the perl-String-CamelCase package.
Group: Default

%description license
license components for the perl-String-CamelCase package.


%package perl
Summary: perl components for the perl-String-CamelCase package.
Group: Default
Requires: perl-String-CamelCase = %{version}-%{release}

%description perl
perl components for the perl-String-CamelCase package.


%prep
%setup -q -n String-CamelCase-0.04
cd %{_builddir}
tar xf %{_sourcedir}/libstring-camelcase-perl_0.04-1.debian.tar.xz
cd %{_builddir}/String-CamelCase-0.04
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/String-CamelCase-0.04/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-CamelCase
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-String-CamelCase/2d349247de26a4c9807dc9ef514fd1c0c65b1349
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::CamelCase.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-CamelCase/2d349247de26a4c9807dc9ef514fd1c0c65b1349

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
