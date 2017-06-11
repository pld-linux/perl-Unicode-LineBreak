#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Unicode
%define		pnam	LineBreak
%include	/usr/lib/rpm/macros.perl
Summary:	Unicode::LineBreak - UAX #14 Unicode Line Breaking Algorithm
Summary(pl.UTF-8):	Unicode::LineBreak - algorytm łamiania linii w Unikodzie UAX #14
Name:		perl-Unicode-LineBreak
Version:	2017.004
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	de7672227922260ac92d20bbad29660b
URL:		http://search.cpan.org/dist/Unicode-LineBreak/
BuildRequires:	libthai-devel >= 0.1.9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	sombok-devel >= 2.4.0
BuildRequires:	sombok-devel < 3
%if %{with tests}
BuildRequires:	perl-Encode >= 1:1.98
BuildRequires:	perl-MIME-Charset >= 1.006.2
%endif
Requires:	sombok >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::LineBreak performs Line Breaking Algorithm described in
Unicode Standard Annex #14 [UAX #14]. East_Asian_Width informative
property defined by Annex #11 [UAX #11] will be concerned to determine
breaking positions.

%description -l pl.UTF-8
Unicode::LineBreak wykonuje algorytm łamania linii opisany w
dokumencie Unicode Standard Annex #14 (UAX #14). Przy określaniu
miejsc łamania brana jest pod uwagę własność informacyjna
East_Asian_Width zdefiniowana w dokumencie Annex #11 (UAX #11).

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Unicode/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/POD2/JA/Text/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/POD2/JA/Unicode/*.pod

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man3
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man3/POD2::JA::Text::LineFold.3pm $RPM_BUILD_ROOT%{_mandir}/ja/man3/Text::LineFold.3pm
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man3/POD2::JA::Unicode::GCString.3pm $RPM_BUILD_ROOT%{_mandir}/ja/man3/Unicode::GCString.3pm
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man3/POD2::JA::Unicode::LineBreak.3pm $RPM_BUILD_ROOT%{_mandir}/ja/man3/Unicode::LineBreak.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/auto/Unicode/LineBreak
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/LineBreak/LineBreak.so
%{perl_vendorarch}/Text/LineFold.pm
%{perl_vendorarch}/Unicode/GCString.pm
%{perl_vendorarch}/Unicode/LineBreak.pm
%dir %{perl_vendorarch}/Unicode/LineBreak
%{perl_vendorarch}/Unicode/LineBreak/Constants.pm
%{_mandir}/man3/Text::LineFold.3pm*
%{_mandir}/man3/Unicode::GCString.3pm*
%{_mandir}/man3/Unicode::LineBreak.3pm*
%lang(ja) %{_mandir}/ja/man3/Text::LineFold.3pm*
%lang(ja) %{_mandir}/ja/man3/Unicode::GCString.3pm*
%lang(ja) %{_mandir}/ja/man3/Unicode::LineBreak.3pm*
