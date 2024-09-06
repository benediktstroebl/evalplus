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
    num_found = 0
    for char in files[0]:
        if char.isdigit():
            num_found += 1
    if num_found > 3:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes a string representing a file's name as input. It checks for the validity of the file name based on several conditions outlined in the problem statement. The function splits the file name into its prefix and suffix using the dot character ('.'). If the split resulted in more than two segments, it indicates invalid naming, causing the function to return "No". An empty prefix or a prefix that does not start with a letter (lowercase or uppercase) is also considered invalid. The script further counts the number of digits present in the prefix and limits the maximum count to three. If these conditions are met, the script checks if the suffix is one of the expected options ("txt," "exe," or "dll") and returns "Yes" if all conditions are satisfied. If any of the conditions are not met, it returns "No." 

This solution provides a robust and concise approach to validating file names in accordance with the specified requirements.