Name:           volk
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        The Vector Optimized Library of Kernels 
Group:          System Environment/Libraries
License:	GPLv3
URL:            https://github.com/gnuradio/volk
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3
BuildRequires:  python-mako
BuildRequires:  python-six
BuildRequires:  boost169-devel
BuildRequires:  orc-devel

%description
The Vector Optimized Library of Kernels

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%package python
Summary:	%{name} python package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description python
Python files for %{name}.

%prep
%setup

%build
cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DBOOST_INCLUDEDIR=/usr/include/boost169/ -DBOOST_LIBRARYDIR=/usr/lib64/boost169/

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README.md 
%{_libdir}/lib%{name}.so.*
%{_bindir}/volk*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%files python
%defattr(-,root,root,-)
/usr/lib64/python2.7/site-packages/volk_modtool/

%changelog
