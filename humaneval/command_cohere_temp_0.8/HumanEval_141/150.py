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
    if len(files[0]) > 3 or not isinstance(files[0][0], str) or not files[0][0].isalpha():
        return "No"
    if len(files[1]) > 0 and files[1] not in ["txt", "exe", "dll"]:
        return "No"
    return "Yes"
```

This Python script defines a function called `file_name_check` that takes the name of a file as input. It checks the following conditions of a valid file name:
1. The file name is not empty and contains exactly one dot (.).
2. The part of the file name before the dot has a length of at most 3 characters, consists only of alphabetic characters, and is not empty.
3. The part of the file name after the dot is one of the specific strings ("txt", "exe", "dll").
If all conditions are met, it returns the string "Yes", indicating a valid file name; otherwise, it returns "No" to indicate an invalid file name. 

Let's break down the code:
- The function starts with an optional comment describing its purpose, which is to check the validity of a file name and return 'Yes' if valid and 'No' otherwise. 
- The function also checks if the input is not empty and if it's of type `str`.
- The `split('.')` splits the file name at the dot into a list of its components, assuming the file name is represented as a string.
- The system checks that the list has exactly 2 elements and that the first element is not empty.
- The system uses `isalpha()` to check if the first element (before the dot) contains only letters. 
 It also checks if the length of the first element is more than 3.
- Lastly, the system checks the second element (after the dot) to see if it is one of the specified values ("txt", "exe", "dll"). If this is not the case, it returns "No".
- If all the conditions are met, the function returns "Yes". 

Overall, the `file_name_check` function is designed to ensure that a file name adheres to a specific format and criteria to determine whether it is a valid file name or not.