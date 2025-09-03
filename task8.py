with open("C:\\Users\\OM\\Documents\\sample.txt","w") as file:
    write=file.write(input("enter the text to write in the file:"))
    print("text written successfully")
with open("C:\\Users\\OM\\Documents\\sample.txt","a") as file1:
    append=file1.write(input("enter the text to append in the file:"))
    print("text appended successfully")
with open("C:\\Users\\OM\\Documents\\sample.txt","r") as file2:
    read=file2.read()
    print("the content of the file is:")
    print(read)
