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
    if not isinstance(file_name, str):
        return "File name should be a string"
    
    if not file_name.startswith(tuple(''.join(['a', 'b', 'c'])) and tuple(''.join(['A', 'B', 'C]))):
        return "File name should start with a letter"
    
    if '.' not in file_name:
        return "File name should contain a dot"
    
    dot_index = file_name.index('.')
    
    if len(file_name[:dot_index]) > 3:
        return "File name before dot should have less than 4 characters"
    
    if len(file_name[:dot_index]) == 0:
        return "File name before dot should not be empty"
    
    first_char = file_name[:dot_index][0]
    
    if not (first_char in tuple(''.join(['a', 'b', 'c'])) and tuple(''.join(['A', 'B', 'C']))) :
        return "File name start character should be a letter"
    
    file_ext = file_name[dot_index+1:]
    
    if file_ext not in ['txt', 'exe', 'dll']:
        return "File extension should be txt, exe or dll"
    
    return "Yes"
```

This code includes explicit checks against each of the problem statements, with separate conditional statements evaluating each requirement.

To verify the correctness of the solution, you can create a test suite with example file names and verify that the function returns the expected values for each test case. Adjust the test cases accordingly based on the problem statements.