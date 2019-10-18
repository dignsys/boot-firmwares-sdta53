%define debug_package %{nil}
Name:       sdta9-boot-firmware
Summary:    Boot firmwares for Anchor5
Version:    1.0.0
Release:    0
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz

%description
Boot firmwares for Anchor5

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

# 1. Destination directories
mkdir -p %{buildroot}/boot/
mkdir -p %{buildroot}/u-boot/

# 2. Install Images
install -m 755 files/uInitrd %{buildroot}/boot/
install -m 755 files/logo.bmp %{buildroot}/boot/
install -m 644 files/bl1-emmcboot.bin %{buildroot}/u-boot/
install -m 644 files/loader-emmc.img %{buildroot}/u-boot/
install -m 644 files/bl_mon.img %{buildroot}/u-boot/
install -m 644 files/bootloader.img %{buildroot}/u-boot/
install -m 644 files/params.bin %{buildroot}/u-boot/

%files
%attr(0644, root, root) /boot/*
%attr(0644, root, root) /u-boot/*
