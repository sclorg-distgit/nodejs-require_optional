%{?scl:%scl_package nodejs-resolve-from}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-require_optional

%global npm_name require_optional
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-require_optional
Version:	1.0.0
Release:	1%{?dist}
Summary:	Allows you declare optionalPeerDependencies that can be satisfied by the top level module but ignored if they are not.
Url:		https://github.com/christkv/require_optional
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	ASL 2.0

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(bson)
BuildRequires:	%{?scl_prefix}npm(co)
BuildRequires:	%{?scl_prefix}npm(es6-promise)
BuildRequires:	%{?scl_prefix}npm(mocha)
%endif

#BuildRequires:	%{?scl_prefix}npm(resolve-from)
#BuildRequires:	%{?scl_prefix}npm(semver)

%description
Allows you declare optionalPeerDependencies that can be satisfied by the top level module but ignored if they are not.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
mocha
%endif

%files
%{nodejs_sitelib}/require_optional

%doc README.md
%doc LICENSE

%changelog
* Wed Apr 06 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-1
- Initial build

