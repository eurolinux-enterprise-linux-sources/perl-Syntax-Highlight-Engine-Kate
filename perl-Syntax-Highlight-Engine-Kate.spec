Name:           perl-Syntax-Highlight-Engine-Kate
Version:        0.07
Release:        5%{?dist}
Summary:        Port to Perl of the syntax highlight engine of the Kate text editor
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Syntax-Highlight-Engine-Kate/
Source0:        http://www.cpan.org/authors/id/S/SZ/SZABGAB/Syntax-Highlight-Engine-Kate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(inc::Module::Install) >= 0.91
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
# Tests only:
BuildRequires:  perl(lib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Differences) >= 0.61
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(base)

%description
Syntax::Highlight::Engine::Kate is a port to perl of the syntax highlight
engine of the Kate text editor.

%prep
%setup -q -n Syntax-Highlight-Engine-Kate-%{version}
rm -r inc/*
rm -rf lib/Syntax/Highlight/Engine/Kate/Alerts
find -type f -exec chmod -x {} +
chmod 644 Changes REGISTERED

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT OPTIMIZE="$RPM_OPT_FLAGS"
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README REGISTERED
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.07-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Petr Pisar <ppisar@redhat.com> - 0.07-3
- Update dependencies

* Wed Sep 26 2012 Petr Pisar <ppisar@redhat.com> - 0.07-2
- Remove unneeded dependencies

* Tue Sep 25 2012 Marcela Mašláňová <mmaslano@redhat.com> - 0.07-1
- 860376 update to 0.07

* Mon Aug 20 2012 Petr Pisar <ppisar@redhat.com> - 0.06-8
- Modernize spec file
- Specify all dependencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.06-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.06-4
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06-2
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Sep 16 2010 Petr Pisar <ppisar@redhat.com> - 0.06-1
- 0.06 bump
- Add new BuildRequires
- Remove merged patch
- Correct summary spelling

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.04-7
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.04-6
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May  5 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.04-4
- add BR

* Mon May  4 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.04-3
- noarch, remove doubled Alerts

* Wed Apr 23 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.04-2
- generate again new spec

* Wed Apr 22 2009 Marcela Mašláňová <mmaslano@redhat.com> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
