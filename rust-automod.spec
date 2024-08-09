# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
%bcond_without check
%global debug_package %{nil}

%global crate automod

Name:           rust-automod
Version:        1.0.14
Release:        1
Summary:        Pull in every source file in a directory as a module
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/automod
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  (crate(proc-macro2/default) >= 1.0.74 with crate(proc-macro2/default) < 2.0.0~)
BuildRequires:  (crate(quote/default) >= 1.0.35 with crate(quote/default) < 2.0.0~)
BuildRequires:  (crate(syn/default) >= 2.0.46 with crate(syn/default) < 3.0.0~)
BuildRequires:  rust >= 1.56

%global _description %{expand:
Pull in every source file in a directory as a module.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(automod) = 1.0.14
Requires:       (crate(proc-macro2/default) >= 1.0.74 with crate(proc-macro2/default) < 2.0.0~)
Requires:       (crate(quote/default) >= 1.0.35 with crate(quote/default) < 2.0.0~)
Requires:       (crate(syn/default) >= 2.0.46 with crate(syn/default) < 3.0.0~)
Requires:       cargo
Requires:       rust >= 1.56

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(automod/default) = 1.0.14
Requires:       cargo
Requires:       crate(automod) = 1.0.14

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
