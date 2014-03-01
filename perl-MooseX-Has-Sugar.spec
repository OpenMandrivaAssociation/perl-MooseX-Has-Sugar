%define upstream_name    MooseX-Has-Sugar%define upstream_version 1.000000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Experimental sweetness
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Find::Lib)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types::Moose)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(namespace::autoclean)

BuildArch:	noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.704.190-1mdv2011.0
+ Revision: 659977
- update to new version 0.05070419

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.50.556.160-2
+ Revision: 657125
- fix br
- rebuild for updated spec-helper

* Mon Nov 15 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.556.160-1mdv2011.0
+ Revision: 597669
- update to new version 0.05055616

* Tue Aug 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.466.110-1mdv2011.0
+ Revision: 570932
- update to 0.05046611

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.443.30-1mdv2011.0
+ Revision: 561035
- update to 0.05044303

* Sat Dec 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.500-1mdv2011.0
+ Revision: 473856
- update to 0.0405

* Wed Aug 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.400-1mdv2010.0
+ Revision: 415570
- import perl-MooseX-Has-Sugar


* Wed Aug 12 2009 cpan2dist 0.0404-1mdv
- initial mdv release, generated with cpan2dist


