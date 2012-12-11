%define upstream_name    Scalar-String
%define upstream_version 0.001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	String aspects of scalars
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Scalar/%{upstream_name}-%{upstream_version}.tar.lzma

BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.1.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Aug 28 2010 Shlomi Fish <shlomif@mandriva.org> 0.1.0-1mdv2011.0
+ Revision: 573811
- import perl-Scalar-String

