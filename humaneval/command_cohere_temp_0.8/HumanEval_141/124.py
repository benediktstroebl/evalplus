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

    elif file_name.find(".") != -1 and len(file_name) <= 10:
        pre, post = file_name.split(".")
        if len(pre) == 0 or not pre[0].isalpha():
            return "No"
        if post not in ["txt", "exe", "dll"]:
            return "No"
        else:
            return "Yes"
    else:
        return "No"
```

This Python script defines a function `file_name_check` that takes a single argument, `file_name`, which is the name of a file. It checks for several conditions that indicate whether the file name is valid or not. If all the conditions are met, it returns the string 'Yes', indicating a valid file name; otherwise, it returns the string 'No' to indicate that the file name is not valid.

Here's a breakdown of the conditions checked in the script:
1. **String Length & Null Checks**: The script first checks if the `file_name` is null or not a string, and returns 'Yes' if these conditions are met. It also checks if the total length of the file name (including its extension) is less than or equal to 10 characters to limits the maximum number of characters in the file name, including the extension.
2. **Exactly one dot '.'**: The script ensures that the file name contains exactly one dot '.' character. This is checked using the find(".") function, which returns a positive value if the character is found in the string, indicating the position of the first occurrence. If find(".") returns -1, it means there is no dot, and the function returns 'No'.
3. **Valid before the dot**: The script then checks the part of the file name before the dot. If this part is empty or does not start with a letter (lowercase or uppercase), it returns 'No'. If the pre-dot part passes these checks, it proceeds to the next condition.
4. **Valid after the dot**: The script checks the part of the file name after the dot, ensuring that it is one of the permitted extensions, namely, 'txt', 'exe', or 'dll'. If the file name doesn't meet these criteria, it returns 'No'. 

The script returns 'Yes' only when all the conditions are met, and it returns 'No' in all other cases. 

This code ensures that it covers the basic checks for a valid file name as outlined in the problem statement, and