Name:           beispiel1
Version:        0.42.23
Release:        0
Summary:        Demo1
License:        GPLv3
Group:          Development/Libraries/Perl
Url:            http://www.b1-systems.de
Source:         hello_world.pl
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl

%description
This package contains a hello world script.

%prep

%build
%check

%install
mkdir -p %{buildroot}/opt/demo/bin
install -m 755 %{S:0} %{buildroot}/opt/demo/bin/
 

%files
%defattr(-,root,root,755)
%dir /opt/demo
%dir /opt/demo/bin
/opt/demo/bin/*

%changelog
