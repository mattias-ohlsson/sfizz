Name:           sfizz
Version:        0.3.0
Release:        1%{?dist}
Summary:        SFZ library and LV2 plugin

# https://github.com/sfztools/sfizz/blob/master/LICENSE.md: BSD
# https://github.com/abseil/abseil-cpp/blob/master/LICENSE: ASL 2.0
License:        BSD and ASL 2.0
URL:            https://sfz.tools/sfizz
Source0:        https://github.com/sfztools/%{name}/archive/%{version}.tar.gz
Source1:        https://github.com/abseil/abseil-cpp/archive/20190808.tar.gz

BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel
BuildRequires:  cmake >= 3.11
BuildRequires:  libatomic

%global common_desc \
A library to load SFZ description files and use them to render music.

%description
%common_desc

%package -n lv2-%{name}-plugins
Summary:        Sfizz plugin in LV2 format

%description -n lv2-%{name}-plugins
%common_desc

This package contains the LV2 plugin.

%package devel
Summary:        Sfizz development files
Requires:       %{name} = %{version}-%{release}
 
%description devel
%common_desc

This package holds header files for building programs that link against Sfizz.

%prep
%autosetup
%setup -D -T -a 1
cp -R abseil-cpp-*/. external/abseil-cpp/

%build
mkdir build
cd build
%cmake -DCMAKE_BUILD_TYPE=Release -DLV2PLUGIN_INSTALL_DIR=%{_libdir}/lv2 ../
%make_build

%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install

%files
%license LICENSE.md external/abseil-cpp/LICENSE
%doc README.md
%{_bindir}/%{name}_jack
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.so.0

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/%{name}.lv2/

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}.hpp
%{_libdir}/lib%{name}.a
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Feb 29 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.3.0-1
- Update to 0.3.0

* Fri Jan 24 2020 <mattias.ohlsson@inprose.com> - 0.2.0-1
- Initial build
