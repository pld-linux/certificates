Summary:	Root CA
Summary(pl):	Certyfikaty
Name:		certificates
Version:	1.0
Release:	1
License:	distributable (?)
Group:		Networking
Source0:	http://www.modssl.org/source/mod_ssl-2.8.15-1.3.28.tar.gz
# Source0-md5:	0f37d6efd51128f696000d73624f5aff
Source1:	cert-split
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Root CA derived from mod_ssl.

%description -l pl
Pakiet zawiera certyfikaty wyci±gniête z mod_ssl.

%prep
%setup -q -n mod_ssl-2.8.15-1.3.28/pkg.sslcfg
install %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/certs
path=`pwd`
cd $RPM_BUILD_ROOT%{_datadir}/certs
$path/cert-split < $path/ca-bundle.crt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/certs
