### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary: 	The Big Brother Data Base
Summary(pl):	The Big Brother Data Base

Name:    	xemacs-bbdb-pkg
%define 	srcname	bbdb
Version: 	1.09
Release:	1


Patch0:  	%{name}-info.patch
Patch1:  	%{name}-perl.patch

### Preamble
License:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-bbdb-pkg
Requires: 	xemacs-edit-utils-pkg
Requires: 	xemacs-gnus-pkg
Requires: 	xemacs-mh-e-pkg
Requires: 	xemacs-rmail-pkg
Requires: 	xemacs-supercite-pkg
Requires: 	xemacs-vm-pkg
Requires: 	xemacs-tm-pkg
Requires: 	xemacs-apel-pkg
Requires: 	xemacs-mail-lib-pkg
Requires: 	xemacs-base-pkg
Prereq:  	/usr/sbin/fix-info-dir
### EndPreamble

%description


%description -l pl 


### Main
%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
(cd man/bbdb; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
install -d $RPM_BUILD_ROOT%{_infodir}
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/*.info*
gzip -9nf lisp/bbdb/README lisp/bbdb/INSTALL lisp/bbdb/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT
### EndMain

### PrePost
%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1
### EndPrePost

### Files
%files
%defattr(644,root,root,755)
%{_datadir}/xemacs-packages/etc/*
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%doc lisp/bbdb/README.gz lisp/bbdb/INSTALL.gz lisp/bbdb/ChangeLog.gz 
### EndFiles
