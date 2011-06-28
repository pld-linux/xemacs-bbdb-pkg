Summary:	The Big Brother Data Base
Summary(pl.UTF-8):	The Big Brother Data Base
Name:		xemacs-bbdb-pkg
%define 	srcname	bbdb
Version:	1.32
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	43b247335800cfe4bd8bb207725abbbb
Patch0:		%{name}-info.patch
Patch1:		%{name}-perl.patch
URL:		http://www.xemacs.org/
BuildRequires:	texinfo
Requires:	xemacs
Requires:	xemacs-apel-pkg
Requires:	xemacs-base-pkg
Requires:	xemacs-bbdb-pkg
Requires:	xemacs-edit-utils-pkg
Requires:	xemacs-gnus-pkg
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-mh-e-pkg
Requires:	xemacs-rmail-pkg
Requires:	xemacs-supercite-pkg
Requires:	xemacs-vm-pkg
Requires:	xemacs-tm-pkg
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Insidious Big Brother Database - a contact management utility.

%description -l pl.UTF-8
The Insidious Big Brother Database - zarządzanie informacjami
kontaktowymi.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
cd man/bbdb
awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc lisp/bbdb/{README,INSTALL,ChangeLog}
%{_datadir}/xemacs-packages/etc/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
%{_infodir}/*.info*
