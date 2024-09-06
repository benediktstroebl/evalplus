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
    # check for only 3 digits maximum in the entire file name
    if len(files[0]) > 3 and files[0].isdigit():
        return "No"
    if not files[0].isalpha():
        return "No"
    if files[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes a string file name as input and returns either "Yes" or "No" depending on the conditions outlined in the problem. The function checks if the file name contains exactly one period, and splits the file name at that period to extract the file extension. It then checks the following rules:
1. Maximum of 3 digits in the file name (excluding extensions).
2. Exactly one period separating the file base and extension.
3. A non-empty file base starting with an alphabet letter.
4. File extension being either "txt", "exe", or "dll". 

The function returns "Yes" if all conditions are met, and "No" otherwise. Feel free to modify the function to handle more complex edge cases or add more robust error handling if needed based on your further use cases.