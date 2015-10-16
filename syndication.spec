%define major 5
%define libname %mklibname KF5Syndication %{major}
%define devname %mklibname KF5Syndication -d

Name: syndication
Version:	15.08.2
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%description
KDE RSS/Atom parser library

%package -n %{libname}
Summary: KDE RSS/Atom parser library
Group: System/Libraries

%description -n %{libname}
KDE RSS/Atom parser library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.4*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
