import ftplib
import os

global ftp
ftp = ftplib.FTP('your_ftp_server', user='your_user_name', passwd='your_password')
print("connected to FTP")

folder_path = "local_folder_path_1"
# iterate over all files in the folder and delete them
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    os.unlink(file_path)
folder_path = "local_folder_path_2"
# iterate over all files in the folder and delete them
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    os.unlink(file_path)
folder_path = "local_folder_path_3"
# iterate over all files in the folder and delete them
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    os.unlink(file_path)

#-----------------------------------------------------------------------------

#update the path
files = ftp.nlst('/EDW-Reports/reports/EB/APN/EDWEB_DAILY_TOTAL_APN_REPORT_2*')
for file in files:
    print(file)

# Loop through each file and retrieve its modified time
modified_times = {}
for file in files:
    modified_time = ftp.sendcmd("MDTM {}".format(file))
    modified_times[file] = modified_time[4:]  # Extract the timestamp from the response
    

# Find the file with the newest modified time
newest_file = max(modified_times, key=modified_times.get)

file_name = os.path.basename(newest_file)
local='E://AdHoc Report/APN/'+file_name
with open(local, 'wb') as f:
    ftp.retrbinary('RETR '+ newest_file, f.write)

print("The file with the newest modified time is: {}".format(file_name))    

#-----------------------------------------------------------------

#update the path
files = ftp.nlst('/EDW-Reports/reports/EB/APN/EDWCR_daily_CORP_Advance_Top_Up_Active_SIM_OBIEE_WITH_CURENT_ABILITY_STATUS_2*')
for file in files:
    print(file)

# Loop through each file and retrieve its modified time
modified_times = {}
for file in files:
    modified_time = ftp.sendcmd("MDTM {}".format(file))
    modified_times[file] = modified_time[4:]  # Extract the timestamp from the response
    

# Find the file with the newest modified time
newest_file = max(modified_times, key=modified_times.get)

file_name = os.path.basename(newest_file)
local='E://AdHoc Report/APN/'+file_name
with open(local, 'wb') as f:
    ftp.retrbinary('RETR '+ newest_file, f.write)

print("The file with the newest modified time is: {}".format(file_name))    
#-----------------------------------------------------------

#update the path
files = ftp.nlst('/EDW-Reports/reports/EB/GSM/GSM_SERVICE_MAST_CORP_INDIVIDUAL_2*')
for file in files:
    print(file)

# Loop through each file and retrieve its modified time
modified_times = {}
for file in files:
    modified_time = ftp.sendcmd("MDTM {}".format(file))
    modified_times[file] = modified_time[4:]  # Extract the timestamp from the response
    

# Find the file with the newest modified time
newest_file = max(modified_times, key=modified_times.get)

file_name = os.path.basename(newest_file)
local='E://AdHoc Report/GSM/'+file_name
with open(local, 'wb') as f:
    ftp.retrbinary('RETR '+ newest_file, f.write)

print("The file with the newest modified time is: {}".format(file_name))    
#-----------------------------------------------------------
#-----------------------------------------------------------

#update the path
files = ftp.nlst('/EDW-Reports/reports/EB/MVPN/EDWEB_DAY_MVPN_PREPAID_2*')
for file in files:
    print(file)

# Loop through each file and retrieve its modified time
modified_times = {}
for file in files:
    modified_time = ftp.sendcmd("MDTM {}".format(file))
    modified_times[file] = modified_time[4:]  # Extract the timestamp from the response
    

# Find the file with the newest modified time
newest_file = max(modified_times, key=modified_times.get)

file_name = os.path.basename(newest_file)
local='E://AdHoc Report/MVPN/'+file_name
with open(local, 'wb') as f:
    ftp.retrbinary('RETR '+ newest_file, f.write)

print("The file with the newest modified time is: {}".format(file_name))    
#-----------------------------------------------------------

ftp.quit()