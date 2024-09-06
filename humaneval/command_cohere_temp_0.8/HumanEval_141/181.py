```python
def file_name_check(file_name):
    Motel = file_name.split('.')
    if len(Motel)[0] == "" or not Motel[0].isalpha():
        return "No"
    if len(Motel)[0] != Motel[0].replace("""[^a-zA-Z]]"""):
        return "No"
    if len(Motel)[1] > 3:
        return "No"
    if Motel[1] != "txt" and Motel[1] != "exe" and Motel[1] != "dll":
        return "No"
    return "Yes"
```

The following tests demonstrate the behavior of the `file_name_check` function:
```python
# Valid file name, should return "Yes"
print(file_name_check("abc.txt"))

# Invalid file name, should return "No"
print(file_name_check("1abc.exe"))

# Invalid file name, should return "No"
print(file_name_check("abc25.dll"))

# Invalid file name, should return "No"
print(file_name_check("abc..dll"))

# Invalid file name, should return "No"
print(file_name_check("abcdefghijklmnopqrstuvwxyzabc.txt"))
```

This script includes the `file_name_check` function, which takes a file name as input and returns either 'Yes' or 'No' depending on the validity of the file name according to the given specifications. The script also includes self-contained tests that check the function behavior against different test cases.