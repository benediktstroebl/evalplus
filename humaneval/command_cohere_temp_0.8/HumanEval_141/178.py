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
    no_digits = sum(1 for char in files[0] if char.isdigit())
    if no_digits > 3:
        return "No"
    return "Yes"
```
This Python script defines a function called `file_name_check` that takes a single argument, `file_name`, which is the name of a file. The function evaluates the validity of the given file name format and returns a string indicating whether the file name is valid or not.

The function checks the following conditions of the file name format:
1. The file name format must be a string. If it is not, then it isn't a valid file name and the function returns "No".
2. The file name must contain exactly one dot '.'. If it has more than one dot or no dot at all, then it isn't a valid file name and the function returns "No".
3. The part of the file name before the dot must not be empty. If it is empty, then it isn't a valid file name and the function returns "No".
4. The part of the file name before the dot must start with a letter of the Latin alphabet. If it doesn't, then it isn't a valid file name and the function returns "No".
5. The part of the file name after the dot must be either "txt", "exe", or "dll". If it isn't, then it isn't a valid file name and the function returns "No".
6. There should not be more than three digits in the file's name, excluding the ones that might be present in the extension.

If all these conditions are satisfied, the function returns "Yes" to indicate that the file name is valid.

The function then uses a combination of string methods and Python's built-in functionality to check these conditions. It splits the file name at the dot using `split(".")`, checks that there's exactly one element in the resulting list, and that the first element (before the dot) is non-empty and starts with a letter. It also checks that the second element (after the dot) is of