#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
#
Name     : php-scrypt
Version  : 2.0.1
Release  : 37
URL      : https://pecl.php.net/get/scrypt-2.0.1.tgz
Source0  : https://pecl.php.net/get/scrypt-2.0.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-scrypt-lib = %{version}-%{release}
Requires: php-scrypt-license = %{version}-%{release}
BuildRequires : buildreq-php
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The source code under this directory is taken from the client for the
Tarsnap online backup system (and released under the 2-clause BSD license
with permission of the author); keeping this code in sync with the Tarsnap
code is highly desirable and explains why there is some functionality
included here which is not actually used by the scrypt file encryption
utility.

%package lib
Summary: lib components for the php-scrypt package.
Group: Libraries
Requires: php-scrypt-license = %{version}-%{release}

%description lib
lib components for the php-scrypt package.


%package license
Summary: license components for the php-scrypt package.
Group: Default

%description license
license components for the php-scrypt package.


%prep
%setup -q -n scrypt-2.0.1
cd %{_builddir}/scrypt-2.0.1
pushd ..
cp -a scrypt-2.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-scrypt
cp %{_builddir}/scrypt-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-scrypt/7c8e8aab480a0e18a56c200792363ecf71e2ef9b || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/scrypt.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-scrypt/7c8e8aab480a0e18a56c200792363ecf71e2ef9b
