
Summary:	PLDHoros KDE4 wallpapers
Summary(pl.UTF-8):	Tapety PLDHoros do KDE4
Name:		kde4-pldhoros-wallpapers
Version:	0
Release:	1
License:	LGPLv3
Group:		X11/Libraries
Source0:	%{name}.tar.gz
# Source0-md5:	5e84904762e2093308f85761a5d9a3a0
URL:		http://livecd.pld-linux.org
BuildRequires:	rpmbuild(macros) >= 1.293
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLDHoros KDE4 wallpapers.

%description -l pl.UTF-8
Tapety PLDHoros do KDE4.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
cp -ar pldhoros $RPM_BUILD_ROOT%{_datadir}/wallpapers/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/wallpapers/pldhoros
