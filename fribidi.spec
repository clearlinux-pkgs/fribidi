#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fribidi
Version  : 0.19.7
Release  : 6
URL      : http://fribidi.org/download/fribidi-0.19.7.tar.bz2
Source0  : http://fribidi.org/download/fribidi-0.19.7.tar.bz2
Summary  : Unicode Bidirectional Algorithm Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: fribidi-bin
Requires: fribidi-lib
Requires: fribidi-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
This is GNU FriBidi
The Free Implementation of the Unicode Bidirectional Algorithm.

%package bin
Summary: bin components for the fribidi package.
Group: Binaries

%description bin
bin components for the fribidi package.


%package dev
Summary: dev components for the fribidi package.
Group: Development
Requires: fribidi-lib
Requires: fribidi-bin
Provides: fribidi-devel

%description dev
dev components for the fribidi package.


%package dev32
Summary: dev32 components for the fribidi package.
Group: Default
Requires: fribidi-lib32
Requires: fribidi-bin
Requires: fribidi-dev

%description dev32
dev32 components for the fribidi package.


%package doc
Summary: doc components for the fribidi package.
Group: Documentation

%description doc
doc components for the fribidi package.


%package lib
Summary: lib components for the fribidi package.
Group: Libraries

%description lib
lib components for the fribidi package.


%package lib32
Summary: lib32 components for the fribidi package.
Group: Default

%description lib32
lib32 components for the fribidi package.


%prep
%setup -q -n fribidi-0.19.7
pushd ..
cp -a fribidi-0.19.7 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522108730
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522108730
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fribidi

%files dev
%defattr(-,root,root,-)
/usr/include/fribidi/fribidi-arabic.h
/usr/include/fribidi/fribidi-begindecls.h
/usr/include/fribidi/fribidi-bidi-types-list.h
/usr/include/fribidi/fribidi-bidi-types.h
/usr/include/fribidi/fribidi-bidi.h
/usr/include/fribidi/fribidi-char-sets-list.h
/usr/include/fribidi/fribidi-char-sets.h
/usr/include/fribidi/fribidi-common.h
/usr/include/fribidi/fribidi-config.h
/usr/include/fribidi/fribidi-deprecated.h
/usr/include/fribidi/fribidi-enddecls.h
/usr/include/fribidi/fribidi-flags.h
/usr/include/fribidi/fribidi-joining-types-list.h
/usr/include/fribidi/fribidi-joining-types.h
/usr/include/fribidi/fribidi-joining.h
/usr/include/fribidi/fribidi-mirroring.h
/usr/include/fribidi/fribidi-shape.h
/usr/include/fribidi/fribidi-types.h
/usr/include/fribidi/fribidi-unicode-version.h
/usr/include/fribidi/fribidi-unicode.h
/usr/include/fribidi/fribidi.h
/usr/lib64/libfribidi.so
/usr/lib64/pkgconfig/fribidi.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfribidi.so
/usr/lib32/pkgconfig/32fribidi.pc
/usr/lib32/pkgconfig/fribidi.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfribidi.so.0
/usr/lib64/libfribidi.so.0.3.6

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfribidi.so.0
/usr/lib32/libfribidi.so.0.3.6
