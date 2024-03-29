#global debug_package %{nil}
%define _empty_manifest_terminate_build 0

%define major 0

%define libname		%mklibname audec %{major}
%define develname	%mklibname audec -d

Name:           libaudec
Version:        0.3.4
Release:        2
Summary:        libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files
License:        GPLv3
Group:          Development/Libraries/C and C++
URL:            https://git.sr.ht/~alextee/libaudec
Source:         https://git.sr.ht/~alextee/libaudec/archive/v%{version}/%{name}-v%{version}.tar.gz
%ifarch %{ix86} %{arm}
Patch0:         libaudec.patch
%endif
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  ffmpeg-devel

%description
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files, 
based on Robin Gareus' audio_decoder code (https://github.com/x42/silan/tree/master/audio_decoder)

This library is meant to be linked in statically to larger projects.

Until version 1.0 is released, the API is subject to change.

%package -n audec
Summary:        libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate
Group:          System/Libraries

%description -n audec
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files


%package -n %{develname}
Summary:        Development files for libaudec
Group:          Development/Libraries/C and C++
Requires:       audec = %{version}

%description -n %{develname}
This package holds the development files for libaudec,
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files

%prep
%setup -q -n libaudec-v%{version}
%autopatch -p1

%ifarch %{ix86} %{arm}
rm -r tests
%endif

%build
%meson -Dffmpeg=enabled \
%meson_build
%ninja_build -C build

%install
%ninja_install -C build

%files -n audec
%{_bindir}/audec

%files -n %{develname}
%{_includedir}/audec/audec.h
%{_libdir}/libaudec.a
%{_libdir}/pkgconfig/audec.pc
%{_libdir}/libaudec.so
