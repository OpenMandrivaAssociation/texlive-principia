Name:		texlive-principia
Version:	58927
Release:	2
Summary:	Notations for typesetting the "Principia Mathematica"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/principia
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/principia.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/principia.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package supports typesetting the Peanese notation in
Volume I of Whitehead and Russell's 1910 "Principia
Mathematica".

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/principia
%doc %{_texmfdistdir}/doc/latex/principia

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
