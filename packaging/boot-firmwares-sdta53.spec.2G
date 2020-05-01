%define debug_package %{nil}
%define buildarch aarch64
Name:       sdta53-boot-firmware
Summary:    Boot firmwares for SDTA53
Version:    1.0.0
Release:    0
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
ExclusiveArch: aarch64
Source0:    %{name}-%{version}.tar.gz

%description
Boot firmwares for SDTA53

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

# 1. Destination directories
mkdir -p %{buildroot}/boot/
mkdir -p %{buildroot}/u-boot/

# 2. Install Images
install -m 755 files-2G/uInitrd %{buildroot}/boot/
install -m 755 files-2G/logo.bmp %{buildroot}/boot/
install -m 644 files-2G/bl1-emmcboot.img %{buildroot}/u-boot/
install -m 644 files-2G/fip-loader-emmc.img %{buildroot}/u-boot/
install -m 644 files-2G/fip-secure.img %{buildroot}/u-boot/
install -m 644 files-2G/fip-nonsecure.img %{buildroot}/u-boot/
install -m 644 files-2G/params.bin %{buildroot}/u-boot/

%files
%attr(0644, root, root) /boot/*
%attr(0644, root, root) /u-boot/*
