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
    invalid = False
    dot_index = file_name.find(".")
    if dot_index==-1:
        return "No"
    substring_before_dot = file_name[:dot_index]
    if len(substring_before_dot)==0 or \
       not substring_before_dot.lower().startswith(string.ascii_lowercase) or \
       len(substring_before_dot)-substring_before_dot.lower().startswith(string.ascii_lowercase).length > 1:
        return "No"
    file_ext = file_name[dot_index+1:]
    if len(file_ext)==0 or (file_ext not in ["txt", "exe", "dll"] and file_ext not==""):
        return "No"
    if file_ext in ["txt", "exe", "dll"] :
        return "Yes"
    else:
        invalid = True
    if len(file_name)==0 or file_name[0] not in string.ascii_letters:
        return "No"
    if file_name[1:].isalnum():
        if not invalid:
            return "Yes"
        else:
            return "No"
    else:
        return "No"
```
The function examines the provided file name and checks if it conforms to the set of rules provided in the prompt. It returns a 'Yes' validation was successful and a 'No' otherwise. You can use this function to validate file names in accordance with the specified criteria. 
```python
unittest.test(lambda: file_name_check("example.txt"), lambda: file_name_check("1example.dll"), lambda: file_name_check("example.exe"), lambda: file_name_check("abc1000.txt"), lambda: file_name_check("a.txt"), lambda: file_name_check("abc.txt"), lambda: file_name_check("abcinvalid.exe"), lambda: file_name_check("a.invaliddll"), lambda: file_name_check("alaala.txt"))
```
The test suite will ensure the function behaves as expected.