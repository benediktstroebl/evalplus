```python
def file_name_check(file_name):
    assert not any(char in file_name for char in '0123456789'), "There should not be more than three digits ('0'-'9') in the file's name"
    assert '.' in file_name, "The file's name contains exactly one dot '.'"
    assert file_name[:file_name.index('.')].isalpha(), "The substring before the dot should not be empty, and it starts with a letter from the latin alphapet ('a'-'z' and 'A'-'Z')"
    assert file_name[-3:].lower() in ['txt', 'exe', 'dll'], "The substring after the dot should be one of these: ['txt', 'exe', 'dll']"
    
    if not any(char in file_name for char in '0123456789') and '.' in file_name and file_name[:file_name.index('.')].isalpha() and file_name[-3:].lower() in ['txt', 'exe', 'dll']:
        return "Yes"
    else:
        return "No"
```

The function `'file_name_check'` above validates various aspects of a file's name. If all the conditions are met, the function returns `Yes`, otherwise it returns `No`. 

This function can be tested by calling it with a string that represents a file's name and checking whether the returned output corresponds to the expected validity of the file's name.