Name:           sfizz
Version:        0.5.1
Release:        1%{?dist}
Summary:        SFZ library and plugin

# README.md
# The sfizz library makes primary use of:
# - libsndfile, licensed under the GNU Lesser General Public License v2.1
# - Abseil, licensed under the Apache License 2.0
# - atomic_queue by Maxim Egorushkin, licensed under the MIT license
# - filesystem by Steffen Schümann, licensed under the BSD 3-Clause license
# - hiir by Laurent de Soras, licensed under the WTFPL v2 license
# The sfizz library also uses in some subprojects:
# - Catch2, licensed under the Boost Software License 1.0
# - benchmark, licensed under the Apache License 2.0
# - LV2, licensed under the ISC license
# - JACK, licensed under the GNU Lesser General Public License v2.1
License:        BSD
URL:            https://sfz.tools/sfizz
Source0:        https://github.com/sfztools/sfizz/releases/download/%{version}/sfizz-%{version}-src.tar.gz

BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel
BuildRequires:  cmake >= 3.11
BuildRequires:  libatomic
BuildRequires:  gcc gcc-c++
BuildRequires:  libX11-devel freetype-devel fontconfig-devel cairo-devel
BuildRequires:  libxcb-devel xcb-util-devel xcb-util-cursor-devel xcb-util-keysyms-devel
BuildRequires:  libxkbcommon-devel libxkbcommon-x11-devel

%global common_desc \
Sfizz is a musical sampler, available as LV2 and VST plugins for musicians, and \
a library for developers.

%description
%common_desc

%package -n lib%{name}
Summary:   Library files for Sfizz

%description -n lib%{name}
%common_desc

This package contains the runtime files for the Sfizz library.

%package -n lv2-%{name}-plugins
Summary:        Sfizz plugin in LV2 format

%description -n lv2-%{name}-plugins
%common_desc

This package contains the LV2 plugin.

%package -n vst3-%{name}-plugins
Summary:        Sfizz plugin in VST3 format

%description -n vst3-%{name}-plugins
%common_desc

This package contains the VST3 plugin.

%package -n lib%{name}-devel
Summary:        Sfizz development files
Requires:       lib%{name} = %{version}-%{release}
 
%description -n lib%{name}-devel
%common_desc

This package holds header files for building programs that link against Sfizz.

%prep
%autosetup

%build
%cmake -DBUILD_SHARED_LIBS=OFF -DSFIZZ_VST=ON -DLV2PLUGIN_INSTALL_DIR=%{_libdir}/lv2 -DVSTPLUGIN_INSTALL_DIR=%{_libdir}/vst3 .
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}_jack
%{_bindir}/%{name}_render

%files -n lib%{name}
%license LICENSE.md
%{_libdir}/lib%{name}.so.*

%files -n lv2-%{name}-plugins
%license lv2/LICENSE.md.in
%{_libdir}/lv2/%{name}.lv2/

%files -n vst3-%{name}-plugins
%license LICENSE.md vst/gpl-3.0.txt
%{_libdir}/vst3/%{name}.vst3/

%files -n lib%{name}-devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_includedir}/%{name}.hpp
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Oct 28 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.5.1-1
- Update to 0.5.1

* Sun Apr 05 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.3.2-1
- Update to 0.3.2

* Tue Mar 24 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.3.1-1
- Update to 0.3.1

* Sat Feb 29 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.3.0-1
- Update to 0.3.0

* Fri Jan 24 2020 <mattias.ohlsson@inprose.com> - 0.2.0-1
- Initial build
