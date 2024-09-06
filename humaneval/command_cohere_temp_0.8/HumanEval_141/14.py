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
    no_digits = sum(1 for char in files[0] if char.isdigit())
    if no_digits > 3:
        return "No"
    return "Yes"
```
This Python script defines a function called `file_name_check` that takes a string representing a file's name as input. It checks for the validity of the file name based on several rules. If the file name is valid, it returns the string 'Yes'. If the file name is not valid, it returns the string 'No'.

The function evaluates whether the given string conforms to the specifications of a valid file name. This is performed in accordance with the provided problem description. The function initially verifies if the file name is empty or not a string, and if so, it returns 'No'. The script then assesses the length of the file name and separates it into its constituent parts. If the file name does not consist of exactly two parts, or if the initial part is empty, it returns 'No'. The script then verifies the initial part of the file name. If it is empty, or does not begin with a letter (lowercase or uppercase), it returns 'No'. Subsequently, the script checks the length of the latter part of the file name, ensuring it is precisely 3 characters long and is among the following: 'txt', 'exe', 'dll'. If the file name does not meet these criteria, the function returns 'No'. The script also checks for more than three digits in the initial part of the file name, and if found, it returns 'No'. If all conditions are met at the conclusion of the function, it returns 'Yes'.