#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-scrypt
Version  : 1.4.2
Release  : 7
URL      : https://pecl.php.net//get/scrypt-1.4.2.tgz
Source0  : https://pecl.php.net//get/scrypt-1.4.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-scrypt-lib = %{version}-%{release}
BuildRequires : buildreq-php

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

%description lib
lib components for the php-scrypt package.


%prep
%setup -q -n scrypt-1.4.2
cd %{_builddir}/scrypt-1.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/scrypt.so
