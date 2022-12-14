Summary:	Lightweight and fast MJPEG-HTTP streamer
Name:		ustreamer
Version:	5.31
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	https://github.com/pikvm/ustreamer/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ef8230570a937c1d3a69431461f0faa4
URL:		https://github.com/pikvm/ustreamer
BuildRequires:	libbsd-devel
BuildRequires:	libevent-devel
BuildRequires:	libgpiod-devel
BuildRequires:	libjpeg-devel
BuildRequires:	systemd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
┬ÁStreamer is a lightweight and very quick server to stream MJPEG video
from any V4L2 device to the net.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	WITH_GPIO=1 \
	WITH_SYSTEMD=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}" \
	MANPREFIX="%{_mandir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md docs/*.md
%lang(ru) %doc README.ru.md
%attr(755,root,root) %{_bindir}/ustreamer
%attr(755,root,root) %{_bindir}/ustreamer-dump
%{_mandir}/man1/ustreamer.1*
%{_mandir}/man1/ustreamer-dump.1*
