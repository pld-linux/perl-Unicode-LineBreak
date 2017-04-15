#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Unicode
%define		pnam	LineBreak
%include	/usr/lib/rpm/macros.perl
Summary:	Unicode::LineBreak - UAX #14 Unicode Line Breaking Algorithm
Name:		perl-Unicode-LineBreak
Version:	2017.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de7672227922260ac92d20bbad29660b
URL:		http://search.cpan.org/dist/Unicode-LineBreak/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-MIME-Charset
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::LineBreak performs Line Breaking Algorithm described in
Unicode Standard Annex #14 [UAX #14]. East_Asian_Width informative
property defined by Annex #11 [UAX #11] will be concerned to determine
breaking positions.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/Unicode/LineBreak
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/LineBreak/*.so
%dir %{perl_vendorarch}/POD2
%dir %{perl_vendorarch}/POD2/JA
%dir %{perl_vendorarch}/POD2/JA/Text
%{perl_vendorarch}/POD2/JA/Text/LineFold.pod
%dir %{perl_vendorarch}/POD2/JA/Unicode
%{perl_vendorarch}/POD2/JA/Unicode/GCString.pod
%{perl_vendorarch}/POD2/JA/Unicode/LineBreak.pod
%{perl_vendorarch}/Text/LineFold.pm
%{perl_vendorarch}/Unicode/*.pm
%{perl_vendorarch}/Unicode/GCString.pod
%{perl_vendorarch}/Unicode/LineBreak.pod
%dir %{perl_vendorarch}/Unicode/LineBreak
%{perl_vendorarch}/Unicode/LineBreak/Constants.pm
%{_mandir}/man3/*
