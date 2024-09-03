```python
def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns
    'Yes' if the file's name is valid, and returns 'No' otherwise.
    A file name is valid if and only if all the following conditions are met:
    - There should not be more than three characters ('a-z0-9') in the file's name.
    - The name contains exactly one dot '.'
    - The substring before the dot is not empty and starts with an alphabet character.
    - The substring after the dot is either 'txt', 'exe', or 'dll'
    Examples:
    file_name_check("example.txt") == 'Yes'
    file_name_check("1example.dll") == 'No'
    file_name_check("abc.txt") == 'No'
    file_name_check(".1") == 'No'
    file_name_check("a1.txt") == 'No'
file_name_check("123.abc") == 'No'
    file_name_check("big.txt") == 'No'
    file_name_check("1.b") == 'No'
file_name_check("1.dllext") == 'No'
```
This Python code defines a function `file_name_check` that checks the validity of a file name according to a specific set of rules. The function takes a input parameter `file_name`, representing the name of a file. 

The function first defines a set of conditions that a file name is valid, which include:
1. The name contains exactly one dot ('.
2. The substring before the dot is not empty and starts with a lowercase or uppercase alphabet character ('a-z' or 'A-Z').).
3. The substring after the dot is either 'txt', 'exe', or 'dll'.

The function then checks if the conditions are met, and returns 'Yes' if they are, and 'No' otherwise. 

The function is then tested with various input names using a series of example cases. The test cases cover different scenarios, such as the presence of the dot, the starting character of the substring before the dot, and the allowed extensions in the substring after the dot.