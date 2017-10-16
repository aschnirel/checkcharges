
import os
import pandas as pd
import csv




#read files from a given directory
mastersource="/Users/addieschnirel/Check_Charges/MASTER_Charges.csv"
#raw_input('Enter the file path name to the Master Charge list: ')

#open master file
ms_df = pd.read_csv(mastersource, header=None)
#print pd.DataFrame.head(ms_df)



#new_header = ms_df.iloc[0] #grab the first row for the header
#ms_df = ms_df[1:] #take the data less the header row
#ms_df.columns = new_header #set the header row as the df header



charges_source ='/Users/addieschnirel/Check_Charges/July_Charges'
#raw_input('Enter the file path name to the folder of charges: ')

for root, dirs, filenames in os.walk(charges_source):
    for f in filenames:
        #print f
        fullpath = os.path.join(charges_source, f)
        log = open(fullpath, 'r')


#print filenames



#loop through all charges in master file


#loop through each charge file
for filename in filenames:
    fullpath = os.path.join(charges_source, filename)
    f= open(fullpath, 'r')
    currentfile = pd.read_csv(f)
    #print pd.DataFrame.head(currentfile)





#check if charge is in one of the 6 files - maybe use conditions to look for.
#if charge from master file is not in any charge file, print which account (address).
#loop through each master file and each charge.
#look for charge in master file.
#if charge is not in masterfile, print which account (address)

#end output is a list of accounts that were in one file but not the other.



#read-an-old-master-record
new_header=ms_df.loc[0] #grab the first row for the header
print("The headers are %s:" %new_header)
ms_df1 = ms_df[1:] #take the data less the header row
ms_df1.columns = new_header #set the header row as the df header
print pd.DataFrame.head(ms_df1)

#read-a-transaction-record

# while  not-at-end-of-BOTH-files
#
#     if  master-key < transaction-key
#     then
# 	write-master-file-from-master-record
# 	read-an-old-master-record
#     else
#     if  master-key = transaction-key
#     then
# 	attempt-to-apply-transaction-to-master-record
# 	read-a-transaction-record
#     else
#     if  master-key > transaction-key
#     then
# 	attempt-to-add-transaction-record
# 	read-a-transaction-record
#     end-if end-if
# end-while

#Here are some of the routines called by the main logic. I went ahead and wrote the read routines in COBOL.

#to read-an-old-master-record
#
#     READ  MASTER-FILE  INTO  MASTER-RECORD-WS
# 	AT END
# 	    MOVE  HIGH-VALUES  TO  MASTER-KEY
#     END-READ.
#
#
# #to read-a-transaction-record
#
#     READ  TRANSACTION-FILE  INTO  TRANSACTION-RECORD-WS
# 	AT END
# 	    MOVE  HIGH-VALUES  TO  TRANSACTION-KEY
#     END-READ.
#
#
# #to attempt-to-apply-tranaction-to-master-record
#
#     if  transaction-code = add
#     then
# 	report-error(adding record with existing key)
#     else
#     if  transaction-code = change
#     then
# 	apply-the-change-to-the-master-record
#     else
#     if  transaction-code = delete
#     then
# 	read-an-old-master-record
#     else
# 	report-error(invalid transaction code)
#     end-if end-if end-if
#
#
# #to attempt-to-add-transaction-record
#
#     if  transaction-code = add
#     then
# 	write-master-file-from-transaction-record
#     else
#     if  transaction-code = change
#     then
# 	report-error(changing non-existent record)
#     else
#     if  transaction-code = delete
#     then
# 	report-error(deleting non-existent record)
#     else
# 	report-error(invalid transaction code)
#     end-if end-if end-if