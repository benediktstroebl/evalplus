```python
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the file's name is valid, and returns 'No' otherwise.
    A file name is valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphabet ('a'-'z' and 'A'-'Z').
    - The substring after the dot is one of these: ['txt', 'exe', 'dll']
    """
    if len(file_name) > 3:
        return "No"
    if len(file_name) == 4 and "." not file_name:
        return "Yes"
    if file_name[-3:] != "txt":
        return "No"
    if file_name[-1] not in ["_", "e", "E", "d", "D"] and \
        file_name[0].isalpha():
        return "Yes"
    return "No"

# Example usage:
print(file_name_check("example.txt"))  # => True
print(file_name_check("1example.dll"))  # => False
```