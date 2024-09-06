```python
def file_name_check(file_name):
    dots = file_name.count('.')
    if dots > 1:
        return "No"
    elif dots == 1 and len(file_name) > 1 and file_name[0] != "." and file_name[0].isalpha():
        if file_name.split(".")[1] in ["txt", "exe", "dll"]:
            return "Yes"
        else:
            return "No"
    else:
        return "No"
```

This Python script defines a function `file_name_check` that takes a string file name as input and returns "Yes" if the file name is valid, and "No" otherwise. The function checks if the file name is valid based on the following conditions:

1. The file name should not have more than one dot ('.').
2. If there is only one dot, the part before the dot should be non-empty and start with a letter.
3. If there is one dot, the part after the dot should be either "txt", "exe", or "dll".

The function returns "Yes" if the file name meets all of these conditions, and "No" otherwise. Feel free to test this code with different valid and invalid file names to ensure it behaves as expected.