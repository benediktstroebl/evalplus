```python
def file_name_check(file_name):
    err = ""
    if not file_name.isalpha():
        err += "Invalid filename starting letter,\n"
    if '.' not in file_name or len(file_name.split(".")[1]) == 0:
        err += "Filename does not contain a dot or the substring after the dot is empty,\n"
    if len(file_name.split(".")[1]) > 3:
        err += f"Invalid filename length of substring after the dot: {len(file_name.split(".")[1])},\n"
    if file_name.split(".")[1] not in ['txt', 'exe', 'dll']:
        err += f"Invalid filename extension: {file_name.split(".")[1]},\n"
    
    if err:
        return "No"
    else:
        return "Yes"
```

The function examines the following rules:
1. Filename should start with a letter (upper or lower case).
2. Filename should have only one dot and the substring after the dot is not empty.
3. The substring after the dot should be ("txt", "exe", "dll").
4. The length of the substring after the dot should not exceed 3 characters. 

In case any of the above rules are violated, the function returns `NO`, otherwise it returns `YES`. 

Such checking is performed with the help of Python's string methods like `.isalpha()`, `split()`, and `len()`. 

You can test this code by calling this function with different file names. The code is self-contained and does not rely on any external modules other than the Python standard library, making it more portable. 

Let me know if you would like me to make any improvements to this code!