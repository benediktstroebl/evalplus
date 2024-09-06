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
    if files[0].strip() == "" or not files[0].strip().isalpha():
        return "No"
    if len(files[1]) != 4 or files[1] not in ["txt", "exe", "dll"]:
        return "No"
    no_of_digits = files[0].strip().replace("/", "").replace("\\", "").replace("*", "").replace("|", "").replace("?", "").count("0123456789")
    if no_of_digits > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, representing a string with a file's name. This function evaluates the validity of the file's name based on specified conditions and returns "Yes" if the name is valid and "No" otherwise. It checks if the file name contains a single dot (.). The substring before the dot should start with a letter of the Latin alphabet and not be empty, while the substring after the dot should be either "txt," "exe," or "dll." Furthermore, the name should not contain more than three digits. The function returns the appropriate response based on these criteria.