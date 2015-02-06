%define		oname	7kaa

Name:		%{oname}-data
Version:	2.13
Release:	3
Summary:	Game data files for Seven Kingdoms: Ancient Adversaries
Group:		Games/Strategy
License:	GPLv2
URL:		http://7kfans.com/
Source0:	http://sourceforge.net/projects/skfans/files/Seven%20Kingdoms%20AA%20Data%20Files/%{name}-%{version}.tar.bz2
Requires:	%{oname} >= %{version}
BuildArch:	noarch

%description
Game data files required to play Seven Kingdoms: Ancient Adversaries game.

%prep
%setup -q -n %{oname}

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{oname}
cp -r * %{buildroot}%{_datadir}/%{oname}/

%files
%doc COPYING README-GameData
%{_datadir}/%{oname}



%changelog
* Fri Mar 23 2012 Andrey Bondrov <abondrov@mandriva.org> 2.13-1
+ Revision: 786273
- imported package 7kaa-data

