try:
    with open("C:\\Users\\OM\\Documents\\sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")