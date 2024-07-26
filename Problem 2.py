""" Problem 2: Write a python function to read from a text file.
               The function will take the name of the text file and display the content of the file."""
 
# Defined a function with file_name as parameter
def read_file(file_name):
    
    # Opens the file in read mode
    file=open(file_name,'r')
    
    # Reads the content of the file and saves it in display
    display=file.read()
    
    # Prints the content
    print(display)

# Calling the function with file name as parameter
read_file("file_1.txt")
