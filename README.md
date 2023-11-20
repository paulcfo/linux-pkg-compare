# README for Ubuntu Package Version Query Script

## Overview
This script is designed to query the Ubuntu package database for specific releases and packages. It helps in comparing package versions across different Ubuntu releases.

## Features
- Query package information for specified Ubuntu releases.
- Compare package versions across two different releases.
- Easy to modify for different packages and releases.

## Requirements
- Python 3
- `requests` module

## Usage
1. **Set Up**: Install the `requests` module using `pip install requests`.
2. **Configuration**:
   - Define the list of packages you want to query in the `packages` list.
   - Set the `old_release` and `new_release` variables to the Ubuntu release versions you want to compare.
3. **Run the Script**: Execute the script to get the package versions for the specified releases.

## Functions
- `get_ubuntu_package_info(release, package)`: Queries the Ubuntu package database for a given release and package.

## Output
- The script outputs two dictionaries:
  - `old_versions`: Contains package information for the older release.
  - `new_versions`: Contains package information for the newer release.

## Notes
- Ensure internet connectivity as the script fetches data from the Ubuntu package database online.
- The script only handles HTTP 200 responses. Other HTTP errors are not explicitly handled.

## License
This script is provided "as is", without warranty of any kind. Use at your own risk.
