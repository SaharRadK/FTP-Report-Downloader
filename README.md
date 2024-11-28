# FTP Report Downloader

This Python script automates the retrieval of the latest reports from an FTP server and organizes them into local folders based on their categories (e.g., APN, GSM, MVPN). It also cleans up old reports from the local directories before downloading the latest files.

## Features
- Connects to an FTP server using `ftplib`.
- Identifies the most recently modified files in specified FTP directories.
- Downloads the newest files for each category (APN, GSM, MVPN).
- Clears outdated reports from local directories before downloading new files.

## Prerequisites
To run this script, you need:
- Python 3.x installed on your system.
- FTP server credentials (username and password).
- Local directories structured to match the script's organization:
  - `E://AdHoc Report/APN/`
  - `E://AdHoc Report/GSM/`
  - `E://AdHoc Report/MVPN/`

## How to Use
1. Update the FTP credentials and server details:
   ```python
   ftp = ftplib.FTP('your_ftp_server', user='your_username', passwd='your_password')
