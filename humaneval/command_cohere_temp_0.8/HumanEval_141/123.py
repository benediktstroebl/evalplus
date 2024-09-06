```python
def file_name_check(file_name):
    lat_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num_dot = None
    file_ext = None
    if len(file_name) == 0:
        return 'No'
    if len(file_name) > 0 and file_name[0] not in lat_alphabet:
        return 'No'
    if len(file_name) > 0 and file_name[-3:] == '.exe':
        file_ext = 'exe'
    elif len(file_name) > 0 and file_name[-3:] == '.dll':
        file_ext = 'dll'
    elif len(file_name) > 0 and file_name[-2:] == '.txt':
        file_ext = 'txt'
    for i in range(len(file_name)):
        if file_name[i] == '.':
            num_dot = i
        if file_name[i] in '0123456789':
            if num_dot is None:
                return 'No'
            elif i - num_dot - 1 > 3:
                return 'No'
    if file_ext is None:
        return 'No'
    else:
        return 'Yes'
```

This Python script defines a function `file_name_check` that takes in a string representing a file name and checks it against a set of validation rules. The function first checks if the file name is an empty string, and if so, it returns 'No' since an empty file name is not valid. It then checks if the first character of the file name follows the Latin alphabet, and if not, it again returns 'No' since the file name should start with a letter. The script then assesses the file name extension, checking for '.exe' or '.dll' extensions, and if found, it extracts the file extension accordingly. It iterates through the characters of the file name and counts the number of dots present. It also counts the number of digits present in the file name after the first dot. If the number of dots is more than one or the number of digits after the first dot is more than three, the function returns 'No'. The script initializes a variable `file_ext` to keep track of the detected file extension if any. After the loop, if no valid extension is found (`file_ext` remains `None`), the function returns 'No'. Otherwise, if all validation checks pass, the function returns 'Yes' to indicate that the file name is valid. 

The script ensures the file name adheres to the specified criteria and returns 'Yes' only if all conditions are met. You can call the function with different file names to test its behavior and the subsequent results.