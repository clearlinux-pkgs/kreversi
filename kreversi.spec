#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kreversi
Version  : 20.08.0
Release  : 21
URL      : https://download.kde.org/stable/release-service/20.08.0/src/kreversi-20.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.0/src/kreversi-20.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.0/src/kreversi-20.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kreversi-bin = %{version}-%{release}
Requires: kreversi-data = %{version}-%{release}
Requires: kreversi-license = %{version}-%{release}
Requires: kreversi-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kreversi-20.08.0
cd %{_builddir}/kreversi-20.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597792530
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1597792530
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kreversi
cp %{_builddir}/kreversi-20.08.0/COPYING %{buildroot}/usr/share/package-licenses/kreversi/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kreversi-20.08.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/kreversi/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang kreversi

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/knotifications5/kreversi.notifyrc
/usr/share/kreversi/pics/default_theme.desktop
/usr/share/kreversi/pics/default_theme.svgz
/usr/share/kreversi/qml/Board.qml
/usr/share/kreversi/qml/CanvasItem.qml
/usr/share/kreversi/qml/Cell.qml
/usr/share/kreversi/qml/Chip.qml
/usr/share/kreversi/qml/Popup.qml
/usr/share/kreversi/qml/Table.qml
/usr/share/kreversi/qml/globals.js
/usr/share/kreversi/sounds/reversi-click.wav
/usr/share/kreversi/sounds/reversi-won.wav
/usr/share/metainfo/org.kde.kreversi.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kreversi/index.cache.bz2
/usr/share/doc/HTML/de/kreversi/index.docbook
/usr/share/doc/HTML/de/kreversi/kreversi1.png
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
/usr/share/package-licenses/kreversi/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kreversi/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kreversi.lang
%defattr(-,root,root,-)

