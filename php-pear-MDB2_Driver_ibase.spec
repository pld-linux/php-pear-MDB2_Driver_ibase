%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_ibase
%define		_status		stable
%define		_pearname	MDB2_Driver_ibase

Summary:	%{_pearname} - ibase MDB2 driver
Summary(pl):	%{_pearname} - sterownik ibase dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	64284f4d533ac4a53ad0aa257bc365f1
URL:		http://pear.php.net/package/MDB2_Driver_ibase/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(interbase)
Requires:	php-common >= 3:5.0.4
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.3.0
Requires:	php-pear-PEAR-core >= 1:1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Firebird/Interbase MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl
Sterownik Firebird/Interbase dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/Driver/Datatype/ibase.php
%{php_pear_dir}/MDB2/Driver/Manager/ibase.php
%{php_pear_dir}/MDB2/Driver/Native/ibase.php
%{php_pear_dir}/MDB2/Driver/Reverse/ibase.php
%{php_pear_dir}/MDB2/Driver/ibase.php
%{php_pear_dir}/MDB2/Driver/Function/ibase.php
%{php_pear_dir}/data/MDB2_Driver_ibase
