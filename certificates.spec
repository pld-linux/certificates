Summary:	Root CA
Summary(pl.UTF-8):	Certyfikaty
Name:		certificates
Version:	1.1
Release:	2
License:	distributable (?)
Group:		Networking
Source0:	http://www.modssl.org/source/mod_ssl-2.8.30-1.3.39.tar.gz
# Source0-md5:	66c1ad26954cb1abe59b42dab54d2cd1
Source1:	cert-split
Source2:	http://www.certum.pl/keys/CA.crt
# Source2-md5:	2c8f9f661d1890b147269d8e86828ca9
Source3:	http://www.certum.pl/keys/level1.crt
# Source3-md5:	a1423d0a2716eddc2e948129d63b9852
Source4:	http://www.certum.pl/keys/level2.crt
# Source4-md5:	57e929555dccb16d6b7eb6ab07fb9ed5
Source5:	http://www.certum.pl/keys/level3.crt
# Source5-md5:	d305b3d49ef2e70a0bc09f4647a6d580
Source6:	http://www.certum.pl/keys/level4.crt
# Source6-md5:	5b4bf1e06a4a2248a43e4da01a7960fd
Source7:	http://www.certum.pl/keys/vs.crt
# Source7-md5:	8d9833b3dabb5b488df74707c08e8d91
Source8:	http://www.certum.pl/keys/na.crt
# Source8-md5:	77c68e597ca434db5883168babb404f8
Source9:	http://www.certum.pl/keys/tsa.crt
# Source9-md5:	d111d52e3ef202f4144858b7078f7bc6
Source10:	http://www.certum.pl/keys/class1.crt
# Source10-md5:	1802be8de554f1a2a4ac3dc4385aaf6d
Source11:	http://www.certum.pl/keys/class2.crt
# Source11-md5:	b94c16ad2df86da03e1317727af3831d
Source12:	http://www.certum.pl/keys/class3.crt
# Source12-md5:	742d2ef3e7f68c635625151b9c60c938
Source13:	http://www.certum.pl/keys/class4.crt
# Source13-md5:	933f3c7ce4b23c53976b9c6213668d8c
Source14:	https://www.verisign.com/support/thawte-roots.zip 
# Source14-md5:	a3709cc0279ef3fca4f86ea775066b18
Source15:	http://www.cacert.org/certs/root.txt
# Source15-md5:	c2b19e437b9d06ce07780c6d1a99f27a
Source16:	http://www.cacert.org/certs/class3.txt
# Source16-md5:	dd1eaf46b691cfc9981ecceb2bd1906f
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains Root CA derived from mod_ssl.

%description -l pl.UTF-8
Pakiet zawiera certyfikaty wyciągnięte z mod_ssl.

%prep
%setup -q -n mod_ssl-2.8.30-1.3.39/pkg.sslcfg
install %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/certs
path=`pwd`
cd $RPM_BUILD_ROOT%{_datadir}/certs
$path/cert-split < $path/ca-bundle.crt
install %{SOURCE2} "Unizeto - Certum Certification Authority.crt"
install %{SOURCE3} "Unizeto - Certum Level I.crt"
install %{SOURCE4} "Unizeto - Certum Level II.crt"
install %{SOURCE5} "Unizeto - Certum Level III.crt"
install %{SOURCE6} "Unizeto - Certum Level IV.crt"
install %{SOURCE7} "Unizeto - Certum Validation Service.crt"
install %{SOURCE8} "Unizeto - Certum Notary Authority.crt"
install %{SOURCE9} "Unizeto - Certum Time-Stamping Authority.crt"
install %{SOURCE10} "Unizeto - old Certum Level I.crt"
install %{SOURCE11} "Unizeto - old Certum Level II.crt"
install %{SOURCE12} "Unizeto - old Certum Level III.crt"
install %{SOURCE13} "Unizeto - old Certum Level IV.crt"
unzip %{SOURCE14} '*.txt'
for I in *.txt; do
	mv "$I" "`echo $I | sed -e 's!txt!crt!'`"
done
install %{SOURCE15} "CAcert - level1.crt"
install %{SOURCE16} "CAcert - level3.crt"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/certs
