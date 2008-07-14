Summary:	LZF compression library
Summary(pl.UTF-8):	Biblioteka kompresji LZF
Name:		liblzf
Version:	3.2
Release:	1
Epoch:		1
License:	BSD-like (or GPL v2 for core - see LICENSE)
Group:		Libraries
Source0:	http://www.goof.com/pcg/marc/data/%{name}-%{version}.tar.gz
# Source0-md5:	1044a4783a2b15d6002471fd35be2685
Patch0:		%{name}-shared.patch
URL:		http://www.goof.com/pcg/marc/liblzf.html
BuildRequires:	autoconf >= 2.50
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

%description -l pl.UTF-8
LZF jest ekstremalnie szybkim (nie tak dużo wolniejszym od memcpy)
algorytmem kompresji. Jest idealny dla programów, które chcą
zaoszczędzić *trochę* miejsca, ale nie kosztem szybkości. Jest idealny
dla powtarzających się danych. Biblioteka jest mała i nie wymaga
żadnej dodatkowej dużej biblioteki. Jest wolnodostępna, więc nie
powinno być problemów z wykorzystaniem go w komercyjnych programach.
Według aktualnego stanu wiedzy algorytm jest wolny od patentów.

%package devel
Summary:	Header files for liblzf
Summary(pl.UTF-8):	Pliki nagłówkowe liblzf
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for libzlf.

%description devel -l pl.UTF-8
Pliki nagłówkowe liblzf.

%package static
Summary:	Static liblzf library
Summary(pl.UTF-8):	Statyczna biblioteka liblzf
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of liblzf library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki liblzf.

%prep
%setup -q
%patch0 -p1

%build
mv -f config.h.in acconfig.h
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes LICENSE README
%attr(755,root,root) %{_bindir}/lzf
%attr(755,root,root) %{_libdir}/liblzf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblzf.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblzf.so
%{_libdir}/liblzf.la
%{_includedir}/lzf.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liblzf.a
