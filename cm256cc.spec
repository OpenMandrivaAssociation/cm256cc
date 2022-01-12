%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

%global optflags %{optflags} -O3

Name:		cm256cc
Version:	1.1.0
Release:	1
Summary:	Fast GF(256) Cauchy MDS Block Erasure Codec in C++
License:	BSD-2-Clause
Group:		Development/Languages/C and C++
URL:		https://github.com/f4exb/cm256cc
Source:		https://github.com/f4exb/cm256cc/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	ninja

%description
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

%package -n %{libname}
Summary:	Fast GF(256) Cauchy MDS Block Erasure Codec in C++
Group:		System/Libraries

%description -n %{libname}
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

%package -n %{devname}
Summary:	Development files for the cm256cc library
Group:		Development/Libraries/C and C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
This is the rewrite in (as much as possible) clean C++ of cm256.
cm256cc is a simple library for erasure codes. From given data it
generates redundant data that can be used to recover the originals.

This subpackage contains libraries and header files for developing
applications that want to make use of libcm256cc.

%package doc
Summary:	Documentation for cm256cc

%description doc
Documentation for cm256cc.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/cm256_rx
%{_bindir}/cm256_test
%{_bindir}/cm256_tx

%files -n %{libname}
%{_libdir}/libcm256cc.so.%{major}*

%files -n %{devname}
%{_includedir}/cm256cc
%{_libdir}/libcm256cc.so
%{_libdir}/pkgconfig/libcm256cc.pc

%files doc
%doc README.md
