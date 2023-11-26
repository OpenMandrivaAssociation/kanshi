%global forgeurl https://git.sr.ht/~emersion/kanshi
 
Name:           kanshi
Version:        1.4.0
Release:        1
Summary:        Dynamic display configuration for Wayland
 
# Overall project license: MIT
#
# protocol/wlr-output-management-unstable-v1.xml:
# The file is licensed under HPND-sell-variant; it is processed to C-compilable
# files by the `wayland-scanner` binary during build and doesn't alter the main
# license of the binary.
License:        MIT
URL:            https://sr.ht/~emersion/kanshi
Source0:        %{forgeurl}/refs/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
 
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(libvarlink)
BuildRequires:  pkgconfig(scdoc) >= 1.9.2
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
 
%description
kanshi allows you to define output profiles that are automatically enabled
and disabled on hotplug. For instance, this can be used to turn a laptop's
internal screen off when docked.
 
This is a Wayland equivalent for tools like autorandr. kanshi can be used
on Wayland compositors supporting the wlr-output-management protocol.
 
 
%prep
%autosetup -p1
 
%build
%meson
%meson_build
 
%install
%meson_install
# install systemd service
install -D -m 0644 -pv %{SOURCE1} %{buildroot}%{_userunitdir}/%{name}.service
 
%post
%systemd_user_post %{name}.service
 
%preun
%systemd_user_preun %{name}.service
 
%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.*
%{_mandir}/man5/%{name}.*
%{_userunitdir}/%{name}.service
