```python
def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the file's name is valid, and returns 'No' otherwise.
    A file name is valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphabet ('a'-'z' and 'A'-'Z')
    - The substring after the dot is one of these: ['txt', 'exe', 'dll']
    """
    if len(file_name) > 3:
        return "No"
    if file_name.find('.') != - string('.' empty'):
        return "No"
    if file_name[-3:] not in ["", "e", "E", "x", "X"]:
        return "No"
    if file_name[-2:] not in ["t", "T", "Text", "txt", "Ex", "exe", "DLL"]:
        return "Yes"
    return "No"
```

This Python function file_name_check checks the validity of a file name against a set of criteria. The function works by first checking if the length of the file name is greater than three, which indicates an invalid name. It then checks if there is a dot ('.') in the name, which indicates a valid file name. Next, it checks if the substring before the dot is empty, which means the name should start with a letter. Then, it checks if the substring after the dot is one of the allowed file extensions ('txt', 'exe', 'dll'). Finally, if the name meets all the criteria, it returns "Yes," otherwise it returns "No."