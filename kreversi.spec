#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kreversi
Version  : 24.05.0
Release  : 65
URL      : https://download.kde.org/stable/release-service/24.05.0/src/kreversi-24.05.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.0/src/kreversi-24.05.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.0/src/kreversi-24.05.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: kreversi-bin = %{version}-%{release}
Requires: kreversi-data = %{version}-%{release}
Requires: kreversi-license = %{version}-%{release}
Requires: kreversi-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kjobwidgets-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package bin
Summary: bin components for the kreversi package.
Group: Binaries
Requires: kreversi-data = %{version}-%{release}
Requires: kreversi-license = %{version}-%{release}

%description bin
bin components for the kreversi package.


%package data
Summary: data components for the kreversi package.
Group: Data

%description data
data components for the kreversi package.


%package doc
Summary: doc components for the kreversi package.
Group: Documentation

%description doc
doc components for the kreversi package.


%package license
Summary: license components for the kreversi package.
Group: Default

%description license
license components for the kreversi package.


%package locales
Summary: locales components for the kreversi package.
Group: Default

%description locales
locales components for the kreversi package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kreversi-24.05.0
cd %{_builddir}/kreversi-24.05.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716513691
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1716513691
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kreversi
cp %{_builddir}/kreversi-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kreversi/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kreversi-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kreversi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kreversi-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kreversi/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kreversi-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/kreversi/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/kreversi-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kreversi/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kreversi-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kreversi/a4c60b3fefda228cd7439d3565df043192fef137 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kreversi
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kreversi
/usr/bin/kreversi

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kreversi.desktop
/usr/share/icons/hicolor/128x128/apps/kreversi.png
/usr/share/icons/hicolor/16x16/actions/lastmoves.png
/usr/share/icons/hicolor/16x16/actions/legalmoves.png
/usr/share/icons/hicolor/16x16/apps/kreversi.png
/usr/share/icons/hicolor/22x22/actions/lastmoves.png
/usr/share/icons/hicolor/22x22/actions/legalmoves.png
/usr/share/icons/hicolor/22x22/apps/kreversi.png
/usr/share/icons/hicolor/32x32/actions/lastmoves.png
/usr/share/icons/hicolor/32x32/actions/legalmoves.png
/usr/share/icons/hicolor/32x32/apps/kreversi.png
/usr/share/icons/hicolor/48x48/actions/lastmoves.png
/usr/share/icons/hicolor/48x48/actions/legalmoves.png
/usr/share/icons/hicolor/48x48/apps/kreversi.png
/usr/share/icons/hicolor/64x64/apps/kreversi.png
/usr/share/icons/hicolor/scalable/actions/lastmoves.svgz
/usr/share/icons/hicolor/scalable/actions/legalmoves.svgz
/usr/share/knotifications6/kreversi.notifyrc
/usr/share/kreversi/qml/Board.qml
/usr/share/kreversi/qml/CanvasItem.qml
/usr/share/kreversi/qml/Cell.qml
/usr/share/kreversi/qml/Chip.qml
/usr/share/kreversi/qml/Popup.qml
/usr/share/kreversi/qml/Table.qml
/usr/share/kreversi/qml/globals.js
/usr/share/kreversi/sounds/reversi-click.wav
/usr/share/kreversi/sounds/reversi-won.wav
/usr/share/kreversi/themes/default.desktop
/usr/share/kreversi/themes/default.svgz
/usr/share/metainfo/org.kde.kreversi.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kreversi/index.cache.bz2
/usr/share/doc/HTML/ca/kreversi/index.docbook
/usr/share/doc/HTML/ca/kreversi/kreversi1.png
/usr/share/doc/HTML/ca/kreversi/kreversi2.png
/usr/share/doc/HTML/de/kreversi/index.cache.bz2
/usr/share/doc/HTML/de/kreversi/index.docbook
/usr/share/doc/HTML/de/kreversi/kreversi1.png
/usr/share/doc/HTML/en/kreversi/actions-lastmoves.png
/usr/share/doc/HTML/en/kreversi/actions-legalmoves.png
/usr/share/doc/HTML/en/kreversi/document-new.png
/usr/share/doc/HTML/en/kreversi/edit-undo.png
/usr/share/doc/HTML/en/kreversi/games-hint.png
/usr/share/doc/HTML/en/kreversi/index.cache.bz2
/usr/share/doc/HTML/en/kreversi/index.docbook
/usr/share/doc/HTML/en/kreversi/kreversi1.png
/usr/share/doc/HTML/en/kreversi/kreversi2.png
/usr/share/doc/HTML/es/kreversi/index.cache.bz2
/usr/share/doc/HTML/es/kreversi/index.docbook
/usr/share/doc/HTML/et/kreversi/index.cache.bz2
/usr/share/doc/HTML/et/kreversi/index.docbook
/usr/share/doc/HTML/fr/kreversi/index.cache.bz2
/usr/share/doc/HTML/fr/kreversi/index.docbook
/usr/share/doc/HTML/fr/kreversi/kreversi1.png
/usr/share/doc/HTML/it/kreversi/index.cache.bz2
/usr/share/doc/HTML/it/kreversi/index.docbook
/usr/share/doc/HTML/nl/kreversi/index.cache.bz2
/usr/share/doc/HTML/nl/kreversi/index.docbook
/usr/share/doc/HTML/pl/kreversi/index.cache.bz2
/usr/share/doc/HTML/pl/kreversi/index.docbook
/usr/share/doc/HTML/pl/kreversi/kreversi1.png
/usr/share/doc/HTML/pt/kreversi/index.cache.bz2
/usr/share/doc/HTML/pt/kreversi/index.docbook
/usr/share/doc/HTML/pt_BR/kreversi/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kreversi/index.docbook
/usr/share/doc/HTML/ru/kreversi/index.cache.bz2
/usr/share/doc/HTML/ru/kreversi/index.docbook
/usr/share/doc/HTML/sv/kreversi/index.cache.bz2
/usr/share/doc/HTML/sv/kreversi/index.docbook
/usr/share/doc/HTML/sv/kreversi/kreversi-configuration.png
/usr/share/doc/HTML/sv/kreversi/kreversi1.png
/usr/share/doc/HTML/uk/kreversi/index.cache.bz2
/usr/share/doc/HTML/uk/kreversi/index.docbook
/usr/share/doc/HTML/uk/kreversi/kreversi1.png
/usr/share/doc/HTML/uk/kreversi/kreversi2.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kreversi/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kreversi/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kreversi/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/kreversi/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kreversi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kreversi/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f kreversi.lang
%defattr(-,root,root,-)

