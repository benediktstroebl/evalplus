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
        return "Yes"

    latin_dict = str.maketrans('', '', string.ascii_lowercase)
    dot_idx = file_name.find('.')

    num_digits = sum(char.isdigit() for char in file_name if char.isdigit())
    if num_digits > 3 or (dot_idx == -1 or dot_idx == 0 or not file_name[0].translate(latin_dict).isalpha()):
        return "No"
    file_ext = file_name[dot_idx + 1:] if dot_idx != -1 else ""
    if not file_ext.lower() in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
```

This Python script defines a function `file_name_check` that takes a `file_name` as input and returns either "Yes" or "No" depending on the conditions outlined in the problem. Here's a brief explanation of the code:
1. It checks if the `file_name` is not empty or not a string, and if so, it returns "Yes" right away without checking the conditions.
2. It uses `str.maketrans()` to create a translation table for lowercase Latin letters, which is then used to check if the first character of the `file_name` (before the dot) is a letter.
3. It finds the index of the dot in the file name using `find()`.
4. It counts the number of digits in the file name using a generator expression and `sum()` function. If there are more than 3 digits, or if there are no digits, it returns "No".
5. It extracts the file extension after the dot using string slicing if the dot is found, and checks if it's one of the allowed extensions ("txt", "exe", "dll"). If not, it returns "No".
6. If all conditions are met, it returns "Yes". 

The script ensures that the file name meets the specified requirements related to digits, the position of the dot, and the file extension to determine if the file name is valid or not.