%define upstream_name    Scalar-String
%define upstream_version 0.001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:    String aspects of scalars
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Scalar/%{upstream_name}-%{upstream_version}.tar.lzma

BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(bytes)
BuildRequires: perl(if)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is about the string part of plain Perl scalars. A scalar has a
string value, which is notionally a sequence of Unicode codepoints, but may
be internally encoded in either ISO-8859-1 or UTF-8. In places, and more so
in older versions of Perl, the internal encoding shows through. To fully
understand Perl strings it is necessary to understand these implementation
details.

This module provides functions to classify a string by encoding and to
encode a string in a desired way.

This module is implemented in XS, with a pure Perl backup version for
systems that can't handle XS.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


