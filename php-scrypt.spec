#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-scrypt
Version  : 1.4.3
Release  : 21
URL      : https://pecl.php.net/get/scrypt-1.4.3.tgz
Source0  : https://pecl.php.net/get/scrypt-1.4.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : buildreq-php
Patch1: PHP-8.patch

%description
The source code under this directory is taken from the client for the
Tarsnap online backup system (and released under the 2-clause BSD license
with permission of the author); keeping this code in sync with the Tarsnap
code is highly desirable and explains why there is some functionality
included here which is not actually used by the scrypt file encryption
utility.

%prep
%setup -q -n scrypt-1.4.3
cd %{_builddir}/scrypt-1.4.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-scrypt
cp %{_builddir}/scrypt-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-scrypt/7c8e8aab480a0e18a56c200792363ecf71e2ef9b
%make_install


%files
%defattr(-,root,root,-)
