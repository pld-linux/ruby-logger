# TODO
# - how to make the gem note appear correct here?
%define	pkgname	logger
Summary:	Simple logging utility
Name:		ruby-%{pkgname}
Version:	1.2.8
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	3ad9ecc459edd25d972a0a3b52110f79
URL:		http://github.com/nahi/logger
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Logger class provides a simple but sophisticated logging utility
that anyone can use because it's included in the Ruby 1.8.x standard
library.

CAUTION: logger is bundled with ruby/1.8 and 1.9 so when you simply do
'require "logger"' in your lib/app, stock logger.rb is used. You need
to declare to use the gem version of logger by 'gem "logger"; require
"logger"' instead.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_vendorlibdir}/%{pkgname}.rb
