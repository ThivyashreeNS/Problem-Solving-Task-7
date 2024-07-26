""" Problem 1: Write a python program using function,
               (a) The function will create a text file with current timestamp.
               (b) The file content should have the content of the current time stamp. """
 
 
#'datetime' module to get the current timestamp
import datetime

# function to create a file with current timestamp
def create_timestamp_file(file_name):
     
     # open the file in w+(read & write) mode, it creates a file if it doesn't exist
     file=open(file_name,"w+")
     
     # Get the current date and time
     current_time = datetime.datetime.now()
     
     # Write the current date and time in the file
     file.write(f"Current Date and Time: {current_time}\n")
     
     # Get the timestamp
     time_stamp= current_time.timestamp()
     
     # Write the timestamp in the file
     file.write(f"Timestamp: {time_stamp}\n")
     
     # seek(0) function to move the file cursor back to the beginning of the file to read the file from start
     file.seek(0)
     print(file.read())
     file.close()

# Define the filename
file="current_timestamp.txt"
create_timestamp_file(file)
