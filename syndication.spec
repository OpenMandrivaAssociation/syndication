%define major 5
%define libname %mklibname KF5Syndication %{major}
%define devname %mklibname KF5Syndication -d

Name: syndication
Version:	5.85.0
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/frameworks/%(echo %{version}|cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE RSS/Atom parser library
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Gettext)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5CoreAddons)
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%description
KDE RSS/Atom parser library

%package -n %{libname}
Summary: KDE RSS/Atom parser library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE RSS/Atom parser library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories5/syndication.*categories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
