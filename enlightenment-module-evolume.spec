
%define		_module_name	evolume
%define		_snap	20060420
Summary:	Enlightenment DR17 module: %{_module_name}
Summary(pl.UTF-8):	Moduł Enlightenmenta DR17: %{_module_name}
Name:		enlightenment-module-%{_module_name}
Version:	0.0.19
Release:	1.%{_snap}.1
License:	GPL
Group:		X11/Window Managers/Tools
#Source0:	http://www.get-e.org/Resources/Modules/_files/%{_module_name}-%{version}.tar.bz2
Source0:	http://sparky.homelinux.org/snaps/enli/e_modules/%{_module_name}-%{_snap}.tar.bz2
# Source0-md5:	b696fa07c5f44112604d06a58d41bee3
URL:		http://www.get-e.org/Resources/Modules/
BuildRequires:	alsa-lib-devel >= 1.0.8
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	enlightenment-devel
BuildRequires:	libtool
BuildRequires:	sed >= 4.0
Requires:	enlightenment
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple desktop sound mixer.

%description -l pl.UTF-8
Prosty mikser na pulpicie.

%prep
%setup -q -n %{_module_name}
sed -e '/moduledir=/s@=.*@="`enlightenment-config --module-dir`"@' \
    -i configure.ac

%build
CFLAGS="%{rpmcflags} -fPIC"; export CFLAGS
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_module_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_module_name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/module.so
%dir %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/systems
%attr(755,root,root) %{_libdir}/enlightenment/modules_extra/%{_module_name}/linux-gnu-*/systems/module_alsa.so
# violates FHS
%{_libdir}/enlightenment/modules_extra/%{_module_name}/*.edj
%{_libdir}/enlightenment/modules_extra/%{_module_name}/*.png
