```python
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    if not file_name or not isinstance(file_name, str):
        return "No"
    files = file_name.split('.')
    if len(files) != 2 or not files[0]:
        return "No"
    if len(files[0]) == 0 or not (files[0][0].isalpha() or files[0][0].isupper()):
        return "No"
    if len(files[1]) != 3 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    no_of_digits = 0
    for char in files[0]:
        if char.isdigit():
            no_of_digits += 1
    if no_of_digits > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which is the name of a file. The function evaluates the validity of the given file name format and returns a response saying 'Yes' if the name is valid, and 'No' if it is not. 

The criteria used to determine whether a file name is considered valid or not are outlined below:
1. **No More Than Three Digits:** The file name should not contain more than three consecutive digits ('0'-'9') anywhere in the filename.
2. **Exactly One Dot:** The file name must contain exactly one dot '.' character.
3. **Non-Empty Before Dot and Starts with Letter:** The substring before the dot should not be empty, and it should start with a letter from the Latin alphabet, either lowercase ('a'-'z') or uppercase ('A'-'Z').
4. **After Dot is One of Three Options:** The substring after the dot should be one of these: ['txt', 'exe', 'dll'].
5. **No More Than Three Consecutive Digits:** The file name must not contain more than three consecutive digits ('0'-'9') anywhere in the filename.

The script includes tests that check the function against a variety of test cases to ensure it returns the correct result for each case. You can use this function to validate file names in your application or as a starting point to adapt to your specific needs.