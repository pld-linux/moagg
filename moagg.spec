Summary:	Mother of all Gravity Games
Summary(pl):	Matka wszystkich gier grawitacyjnych
Name:		moagg
Version:	0.16
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
# Source0-md5:	e989f21b94639df2a3c2de07d38e0886
Source1:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-data.tar.bz2
# Source1-md5:	ed20870986bcc0fe4ac399e97f66f0e3
URL:		http://moagg.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	freetype-devel >= 2.1.0
BuildRequires:	paragui1-devel >= 1.0.4
BuildRequires:	paragui1-devel < 1.1.0
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moagg combines several game types of other genres like races, search &
rescue, seek & destroy et cetera into a 2D gravity game. You are pilot
of a small space ship and have to navigate that ship through different
levels. But beside the gravity that drags you down there are other
obstacles like laser ports, magnets, black holes, cannons, rockets and
grinders you have to master.

%description -l pl
Moagg ��czy kilka rodzaj�w gier innych gatunk�w, takich jak wy�cigi,
znajd�-i-uratuj, znajd�-i-zniszcz itp., w dwuwymiarow� gr�
grawitacyjn�. Gracz jest pilotem ma�ego statku kosmicznego i musi
kierowa� statkiem poprzez r�ne poziomy. Opr�cz �ci�gaj�cej w d�
grawitacji s� jeszcze inne przeszkody, jak porty laserowe, magnesy,
czarne dziury, dzia�a, rakiety i zgniatacze, nad kt�rymi trzeba
zapanowa�.

%prep
%setup -q -b1

%build
sed -i -e 's#paragui-config#paragui1-config#g' configure* *.m4
cp -f /usr/share/automake/config.* .
SDL_VIDEODRIVER=dummy; export SDL_VIDEODRIVER
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man6/*
