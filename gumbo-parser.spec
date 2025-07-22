%define bname   gumbo
%define libname %mklibname %{bname}
%define devname %mklibname %{bname} -d

Name:		gumbo-parser
Version:	0.13.1
Release:	1
Source0:	https://codeberg.org/gumbo-parser/gumbo-parser/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Gumbo is an implementation of the HTML5 parsing algorithm implemented as a pure C99 library with no outside dependencies.
URL:		https://codeberg.org/gumbo-parser/gumbo-parser
License:	GPL
Group:		Networking/Other

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as a pure C99 library with no outside dependencies. It's designed to serve as a building block for other tools and libraries such as linters, validators, templating languages, and refactoring and analysis tools.


BuildRequires:  ninja
BuildRequires:  pkgconfig(gtest)

BuildSystem:    meson
BuildOption:    -Dcpp_std=c++17

%package -n %{libname}
Summary:    Pure C HTML5 parser
Group:  System/Libraries
Provides:   %{bname} = %{version}-%{release}
Provides:   %{name} = %{version}-%{release}
%description -n %{libname}
Gumbo is an implementation of the HTML5 parsing algorithm implemented as a pure C99 library with no outside dependencies. It's designed to serve as a building block for other tools and libraries such as linters, validators, templating languages, and refactoring and analysis tools.

%package -n %{devname}
Summary:    Headers for developing programs that will use gumbo-parser
Group:  Development/C
Requires:   %{libname} = %{version}-%{release}
Provides:   %{bname}-devel = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
%description -n %{devname}
Headers needed to develop applications using the gumbo-parser HTML5 parser.



%files -n %{libname}

%files -n %{devname}
