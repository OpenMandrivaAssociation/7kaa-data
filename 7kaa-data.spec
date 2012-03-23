%define		oname	7kaa

Name:		%{oname}-data
Version:	2.13
Release:	%mkrel 1
Summary:	Game data files for Seven Kingdoms: Ancient Adversaries
Group:		Games/Strategy
License:	GPLv2
URL:		http://7kfans.com/
Source0:	http://sourceforge.net/projects/skfans/files/Seven%20Kingdoms%20AA%20Data%20Files/%{name}-%{version}.tar.bz2
Requires:	%{name} >= %{version}
BuildArch:	noarch

%description
Game data files required to play Seven Kingdoms: Ancient Adversaries game.

%prep
%setup -q -n %{oname}

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/%{oname}
%__cp -r * %{buildroot}%{_datadir}/%{oname}/

%clean
%__rm -rf %{buildroot}

%files
%doc COPYING README-GameData
%{_datadir}/%{oname}

