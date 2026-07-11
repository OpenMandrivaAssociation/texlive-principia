%global tl_name principia
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.4
Release:	%{tl_revision}.1
Summary:	Notations for typesetting the Principia Mathematica
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/principia
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/principia.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/principia.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package supports typesetting the Peanese notation in Volumes I-III
of Whitehead and Russell's 1910 "Principia Mathematica".

