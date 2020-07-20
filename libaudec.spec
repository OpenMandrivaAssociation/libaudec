%global debug_package %{nil}

%define major 0

%define libname		%mklibname audec %{major}
%define develname	%mklibname audec -d

Name:           libaudec
Version:        0.2.2
Release:        1
Summary:        libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files
License:        GPLv3
Group:          Development/Libraries/C and C++
URL:            https://git.sr.ht/~alextee/libaudec
Source:         https://git.sr.ht/~alextee/libaudec/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  ffmpeg-devel

%description
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files, 
based on Robin Gareus' audio_decoder code (https://github.com/x42/silan/tree/master/audio_decoder)

This library is meant to be linked in statically to larger projects.

Until version 1.0 is released, the API is subject to change.

%package -n %{libname}
Summary:        libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files
Group:          System/Libraries

%description -n %{libname}
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files

%package -n %{develname}
Summary:        Development files for libaudec
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{develname}
This package holds the development files for libaudec,
libaudec (lib audio decoder) is a wrapper library over ffmpeg, sndfile and libsamplerate for reading and resampling audio files

%prep
%setup -q -n libaudec-v%{version}

%build
%meson
%meson_build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}

%files -n %{develname}
