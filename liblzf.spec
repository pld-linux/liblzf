Summary:	LZF compression library
Summary(pl):	Biblioteka kompresji LZF
Name:		liblzf
Version:	0.4
Release:	1
License:	BSD-like
Group:		Libraries
Vendor:		Marc Lehmann <pcg@goof.com>
Source0:	http://www.goof.com/pcg/marc/data/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
URL:		http://www.goof.com/pcg/marc/liblzf.htm
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to
save *some* space but not at the cost of speed. It is ideal for
repetitive data as well. The library is self-contained and very small
(no large library to be pulled in). It is also free, so there should
be no problems incoporating this library into commercial programs. It
is believed that it is free from any patents.

%description -l pl
LZF jest ekstremalnie szybkim (nie tak du¿o wolniejszym od memcpy)
algorytmem kompresji. Jest idealny dla programów, które chc±
zaoszczêdziæ *trochê* miejsca, ale nie kosztem szybko¶ci. Jest idealny
dla powtarzaj±cych siê danych. Biblioteka jest ma³a i nie wymaga
¿adnej dodatkowej du¿ej biblioteki. Jest wolnodostêpna, wiêc nie
powinno byæ problemów z wykorzystaniem go w komercyjnych programach.
Wed³ug aktualnego stanu wiedzy algorytm jest wolny od patentów.

%package devel
Summary:	Header files for liblzf
Summary(pl):	Pliki nag³ówkowe liblzf
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libzlf.

%description devel -l pl
Pliki nag³ówkowe liblzf.

%package static
Summary:	Static liblzf library
Summary(pl):	Statyczna biblioteka liblzf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of liblzf library.

%description static -l pl
Statyczna wersja biblioteki liblzf.

%prep
%setup -q
%patch0 -p1

%build
mv -f config.h.in acconfig.h
%{__libtoolize}
aclocal
autoheader
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbon/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
