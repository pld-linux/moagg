Summary:	Mother of all Gravity Games
Name:		moagg
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
# Source0-md5:	b4ca6fd17db348109665fa4d541f4a76
Source1:        http://dl.sourceforge.net/%{name}/%{name}-%{version}-data.tar.bz2
# Source1-md5:	67aad12e1cb8abd908729d2b76768040
URL:		http://moagg.sourceforge.net/
BuildRequires:	expat-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	freetype-devel
BuildRequires:	paragui1-devel >= 1.0.4
BuildRequires:  paragui1-devel < 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moagg combines several game types of other genres like races, search & rescue, seek & destroy et cetera into a 2D gravity game. You are pilot of a small space ship and have to navigate that ship through different levels. But beside the gravity that drags you down there are other obstacles like laser ports, magnets, black holes, cannons, rockets and grinders you have to master.

%prep
%setup -q -b1

%build
sed -i -e 's#paragui-config#paragui1-config#g' configure* *.m4
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
