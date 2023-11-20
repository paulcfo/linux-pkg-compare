import requests

def get_ubuntu_package_info(release, package):
    """
    Query the Ubuntu package database for a specific release and package.
    """
    response = requests.get(f"https://packages.ubuntu.com/{release}/{package}")
    if response.status_code == 200:
        return response.text
    else:
        return None

# List of packages to query
packages = [
    "php-symfony", "fedora-security", "libnghttp2-14", "grub2-common", "vim-common",
    "python3-twisted", "libtiff5", "libpython3.6-minimal", "libcap2", "libbind9-160",
    "libcups2", "libx11-6", "perl-base", "python3-requests", "openssh-sftp-server",
    "libfuse", "nmap", "libgnutls30", "binutils-x86-64-linux-gnu", "openssh-sftp-server",
    "python-httplib2", "system-sysv", "open-iscsi", "python3-jinja2", "busybox-static",
    "liblxc-common", "system", "libcurl4", "bind9-host", "gcc", "git-man"
]

# Releases to compare
old_release = "bionic"
new_release = "jammy"

# Query the package versions for each release
old_versions = {}
new_versions = {}

for package in packages:
    old_versions[package] = get_ubuntu_package_info(old_release, package)
    new_versions[package] = get_ubuntu_package_info(new_release, package)

old_versions, new_versions

