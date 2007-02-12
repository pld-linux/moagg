Summary:	Mother of all Gravity Games
Summary(pl.UTF-8):   Matka wszystkich gier grawitacyjnych
Name:		moagg
Version:	0.18
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
# Source0-md5:	dee065c819e8d87d9163567e99da192d
Source1:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-data.tar.bz2
# Source1-md5:	282fc0c5ed9552488f2b7d65428d288c
URL:		http://moagg.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
BuildRequires:	cppunit-devel >= 1.10.0
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	paragui1-devel >= 1.0.4
BuildRequires:	paragui1-devel < 1.1.0
BuildRequires:	tetex
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moagg combines several game types of other genres like races, search &
rescue, seek & destroy et cetera into a 2D gravity game. You are pilot
of a small space ship and have to navigate that ship through different
levels. But beside the gravity that drags you down there are other
obstacles like laser ports, magnets, black holes, cannons, rockets and
grinders you have to master.

%description -l pl.UTF-8
Moagg łączy kilka rodzajów gier innych gatunków, takich jak wyścigi,
znajdź-i-uratuj, znajdź-i-zniszcz itp., w dwuwymiarową grę
grawitacyjną. Gracz jest pilotem małego statku kosmicznego i musi
kierować statkiem poprzez różne poziomy. Oprócz ściągającej w dół
grawitacji są jeszcze inne przeszkody, jak porty laserowe, magnesy,
czarne dziury, działa, rakiety i zgniatacze, nad którymi trzeba
zapanować.

%prep
%setup -q -b1

%build
sed -i -e 's#paragui-config#paragui1-config#g' configure* *.m4
cp -f /usr/share/automake/config.* .
SDL_VIDEODRIVER=dummy; export SDL_VIDEODRIVER
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"
cd doc
for i in {internals,level,moagg};
 do
 /usr/bin/texi2html $i.tex
 done
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
