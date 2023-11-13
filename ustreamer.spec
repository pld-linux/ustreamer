#
# Conditional build:
%bcond_without	libgpiod	# GPIO support

Summary:	Lightweight and fast MJPEG-HTTP streamer
Summary(pl.UTF-8):	Lekki i szybki program do emisji strumieni MJPEG-HTTP
Name:		ustreamer
Version:	5.45
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
#Source0Download: https://github.com/pikvm/ustreamer/tags
Source0:	https://github.com/pikvm/ustreamer/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6709d4eef26ec6e0c8831f877152373e
URL:		https://github.com/pikvm/ustreamer
BuildRequires:	libbsd-devel
BuildRequires:	libevent-devel
%{?with_libgpiod:BuildRequires:	libgpiod-devel < 2}
BuildRequires:	libjpeg-devel
BuildRequires:	systemd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uStreamer is a lightweight and very quick server to stream MJPEG video
from any V4L2 device to the net.

%description -l en.UTF-8
µStreamer is a lightweight and very quick server to stream MJPEG video
from any V4L2 device to the net.

%description -l pl.UTF-8
µStreamer to lekki i bardzo szybki serwer strumieni obrazu MJPEG z
dowolnego urządzenia V4L2 do sieci.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	%{?with_libgpiod:WITH_GPIO=1} \
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
%attr(755,root,root) %{_bindir}/ustreamer
%attr(755,root,root) %{_bindir}/ustreamer-dump
%{_mandir}/man1/ustreamer.1*
%{_mandir}/man1/ustreamer-dump.1*
