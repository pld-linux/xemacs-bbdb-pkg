Summary:	The Big Brother Data Base
Summary(pl):	The Big Brother Data Base
Name:		xemacs-bbdb-pkg
%define 	srcname	bbdb
Version:	1.17
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(da):	Programmer/Tekstbehandlere/Emacs
Group(de):	Applikationen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(is):	Forrit/Ritlar/Emacs
Group(it):	Applicazioni/Editor/Emacs
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥¨¥Ç¥£¥¿/Emacs
Group(no):	Applikasjoner/Editorer/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	Aplicações/Editores/Emacs
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/òÅÄÁËÔÏÒÙ/Emacs
Group(sl):	Programi/Urejevalniki/Emacs
Group(sv):	Tillämpningar/Editorer/Emacs
Group(uk):	ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ/òÅÄÁËÔÏÒÉ/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
Patch0:		%{name}-info.patch
Patch1:		%{name}-perl.patch
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-bbdb-pkg
Requires:	xemacs-edit-utils-pkg
Requires:	xemacs-gnus-pkg
Requires:	xemacs-mh-e-pkg
Requires:	xemacs-rmail-pkg
Requires:	xemacs-supercite-pkg
Requires:	xemacs-vm-pkg
Requires:	xemacs-tm-pkg
Requires:	xemacs-apel-pkg
Requires:	xemacs-mail-lib-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Insidious Big Brother Database - a contact management utility.

%description -l pl
The Insidious Big Brother Database - zarz±dzanie informacjami
kontaktowymi.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
(cd man/bbdb; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f  $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

gzip -9nf lisp/bbdb/README lisp/bbdb/INSTALL lisp/bbdb/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/bbdb/README.gz lisp/bbdb/INSTALL.gz lisp/bbdb/ChangeLog.gz 
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
