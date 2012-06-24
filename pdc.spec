Summary:	PDC - the programmers desktop calculator
Summary(pl.UTF-8):	PDC - desktopowy kalkulator dla programistów
Name:		pdc
Version:	0.8.1
Release:	1
License:	GPL
Group:		Applications/Math
Source0:	http://www.redfelineninja.dsl.pipex.com/software/%{name}-%{version}.tar.gz
# Source0-md5:	ec3595e2707a44e9f5372226ac91ab46
URL:		http://www.redfelineninja.dsl.pipex.com/software/all.html#pdc
BuildRequires:	bison
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDC is a desktop calculator similar to bc but with features designed
for use by programmers. In particular PDC supports most ANSI C
operators including bitwise operators and shifts. PDC also makes
dealing with mixed bases very easy since it supports contant pefixes
(eg 0xff, 0755).

%description -l pl.UTF-8
PDC jest desktopowym kalkulatorem podobnym do bc, ale z dodatkami
przeznaczonymi do wykorzystania przez programistów. W szczególności
PDC obsługuje większość operatorów ANSI C włącznie z operatorami
bitowymi i przesunięciami. PDC obsługuje także bardzo łatwo liczby o
różnych podstawach dzięki obsłudze prefiksów (np 0xff, 0755).

%prep
%setup -q

%build
bison %{name}.y
%{__cc} %{rpmldflags} %{rpmcflags} %{name}.tab.c -o %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
