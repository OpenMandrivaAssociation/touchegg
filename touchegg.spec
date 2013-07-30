Name:		touchegg
Version:	1.1
Release:	1
Group:		Graphical desktop/Other
License:	GPLv3
Summary:	Multi-touch gestures recognizer
Url:		https://code.google.com/p/touchegg
Source0:	http://touchegg.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-1.1-qmakepro.patch
BuildRequires:	pkgconfig(libgeis)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(xtst)

%description
Touchégg is a multi-touch gestures recognizer written in C++ 
using the Qt 4 and geis

%prep
%setup -q
%patch0 -p1 -b .qmakepro

%build
%qmake_qt4
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
