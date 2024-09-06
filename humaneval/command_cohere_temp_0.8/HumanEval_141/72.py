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
    files = file_name.split(".")
    if len(files) != 2:
        return "No"
    if len(files[0]) == 0 or not files[0][0].isalpha():
        return "No"
    if len(files[1]) != 4 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    number_of_digits = sum(char.isdigit() for char in files[0])
    if number_of_digits > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which represents the name of a file. The function evaluates the validity of the given file name based on a set of predefined rules and returns either "Yes" or "No" depending on whether the file name meets these criteria or not. 

Here's what's checked in order:
1. The function first checks if the `file_name` is not empty or not a string, and if so, it immediately returns "No".
2. It then checks if the file name contains exactly one dot '.'. If not, or if there are multiple dots, it returns "No".
3. The substring before the dot is checked to ensure it is not empty and starts with a letter (both lowercase and uppercase letters are acceptable). If not, it returns "No".
4. The substring after the dot is checked to ensure it is one of the specified options: "txt", "exe", or "dll". If not, it returns "No".
5. Lastly, the function checks the number of digits in the part of the file name before the dot, ensuring there are not more than three digits. If there are more than three digits, it returns "No".

Overall, this script provides a convenient way to validate file names based on a specific set of rules, and it returns "Yes" if all the conditions are met, and "No" otherwise. 

The script is self-contained and does not rely on any external variables or functions, making it easy to use and integrate into larger projects as needed.