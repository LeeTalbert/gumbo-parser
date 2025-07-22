%define bname   gumbo

Name:		gumbo-parser
Version:	0.13.1
Release:	1
Source0:	https://codeberg.org/gumbo-parser/gumbo-parser/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Gumbo is an implementation of the HTML5 parsing algorithm implemented as a pure C99 library with no outside dependencies.
URL:		https://codeberg.org/gumbo-parser/gumbo-parser
License:	GPL
Group:		Networking/Other

BuildRequires:  pkgconfig(gtest)

BuildSystem:    meson
BuildOption:    -Dcpp_std=c++17

%description
Gumbo is an implementation of the HTML5 parsing algorithm implemented as a pure C99 library with no outside dependencies. It's designed to serve as a building block for other tools and libraries such as linters, validators, templating languages, and refactoring and analysis tools.

%install -a
%libpackages
echo %{_includedir}/tag_enum.h >>%{specpartsdir}/%{mklibname -d gumbo}.specpart
echo %{_includedir}/%{bname}.h >>%{specpartsdir}/%{mklibname -d gumbo}.specpart
