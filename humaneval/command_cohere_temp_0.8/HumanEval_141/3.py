```python
def file_name_check(file_name):
    lilies, ext = 0, 0
    dot_index = file_name.find(".")
    if dot_index==-1 or len(file_name)<=dot_index+1 or not file_name[0].isalpha():
        return "No"
    lilies = file_name[:dot_index]
    ext = file_name[dot_index+1:]
    if lilies[:-1].count("0123456789")>3 or ext not in ["txt", "exe", "dll"] or lilies[-1]==".":
        return "No"
    return "Yes"
```

The script defines a function `file_name_check` that takes a string representing a file's name and returns 'Yes' if the file's name is valid, and 'No' otherwise.

The script implements the following logic:
1. The function first checks if the file name contains a dot or not. If not, then it returns 'No' as the file name is not valid.
2. If the file name contains a dot, the function will check if the substring before the dot is valid. This is done by checking if the substring before the dot contains more than three digits, if it is empty, or if it starts with a letter. If any of these conditions are false, this returns 'No'.
3. The function also checks if the substring after the dot is one of the valid options, i.e., 'txt', 'exe', or 'dll'. If this is not true, then it returns 'No'.
4. If the previous conditions are met, the function returns 'Yes'. 

The `lilies` and `ext` are used to provide more meaningful names to the variables used in the above logic, but they are not used in the final return statement.

The function is designed to be self-contained and does not rely on any external modules or assumptions. 

This solution should be compatible with Python 3.