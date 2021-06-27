Name: libleptonica
Version: 1.81.1
Release: alt1

License: Leptonica license (BSD-like)
Group: System/Libraries
Url: http://www.leptonica.com
Packager: Evgeny Chuck <koi at altlinux.org>

Source: %name-%version.tar
# Source-url: https://github.com/DanBloomberg/leptonica/releases/download/v%version/leptonica-v%version.tar.gz
Patch: %name-1.81.0-alt-makefile.patch

# Automatically added by buildreq on Mon May 31 2021 (-bi)
# optimized out: elfutils glibc-kernheaders-generic glibc-kernheaders-x86 perl pkg-config python-base sh4 termutils zlib-devel

BuildRequires: libgif-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: zlib-devel
# BuildRequires: libopenjpeg2.0-devel (no in р9)
Provides: leptonica = %version-%release
Obsoletes: leptonica = 1.80.0

Summary: A library for manipulating images
Summary(ru_RU.UTF-8): Библиотека для операций над изображениями

%description
This package contains a general library of Leptonica functions for download,
managing and saving image files; and helper utilities for converting image
files, PDF files, and extracting strings from arrays.

%description -l ru_RU.UTF-8
Этот пакет содержит общую библиотеку функций Leptonica для загрузки,
управления и сохранения файлов изображений; и вспомогательные утилиты для
преобразования файлов изображений, файлов PDF и извлечения строк из массивов.

%package devel
Summary: Development files for programs which will use the Leptonica library
Summary(ru_RU.UTF-8): Заголовочные файлы для программ, использующих библиотеку Leptonica
Group: Development/C

Requires: glibc-devel
Requires: libcurl-devel
Requires: libssl-devel
Requires: zlib-devel
Requires: libjpeg-devel
Requires: libtiff-devel
Requires: libpng-devel
Requires: %name = %version-%release 

%description devel
The %name-devel package contains header files for
developing applications that use %name.

%description -l ru_RU.UTF-8 devel
Пакет %name-devel содержит заголовочные файлы для
разработки приложений, использующих %name.

%package devel-static
Summary: Static Leptonica library
Summary(ru_RU.UTF-8): Версия библиотеки Leptonica для статического связывания
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package includes static library necessary for developing statically
which use Leptonica library.

%description -l ru_RU.UTF-8 devel-static
Этот пакет включает в себя статические библиотеки, необходимые для статической
разработки, которая использует библиотеку Leptonica.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
# link to a non-existent file
rm -f %buildroot%_libdir/*.la

%files
# License and notes are needed in the main package, it makes no sense to separate them into another package
%doc README.html
%doc version-notes.html
%doc leptonica-license.txt
%_libdir/*.so.*
# utilities for working with files
# without them, the work with the program will be incomplete
%_bindir/*

%files devel
%_includedir/leptonica
%_libdir/liblept.so
%_libdir/libleptonica.so
%_pkgconfigdir/lept.pc
%_libdir/cmake/LeptonicaConfig-version.cmake
%_libdir/cmake/LeptonicaConfig.cmake

%files devel-static
%_libdir/*.a

%changelog
* Sun Jun 27 2021 Evgeny Chuck <koi@altlinux.org> 1.81.1-alt1
- initial build for ALT Sisyphus

* Sat Jun 12 2021 Koi <eg.evgeniy@gmail.com> 1.81.1-alt1.1
- Add new version 1.81.1

* Mon May 31 2021 Koi <eg.evgeniy@gmail.com> 1.80.0-alt1
- Initial release for ALT Linux Club
