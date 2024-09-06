```python
# Importing the necessary module
from typing import List

# The function to be defined and solved
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated_strings = ""
    for string in strings:
        concatenated_strings += string
    return concatenated_strings
```
The function concatenate takes a list of strings as input and returns a single string that concatenates all the strings in the list. It initializes an empty string, concatenated_strings, and uses a for loop to iterate over each string in the input list. For each string, it appends its content to the concatenated_strings. 

This code snippet will successfully solve the problem of concatenating a list of strings into a single string. You can further verify the functionality of this code through testing. Let me know if you would like me to provide some test cases to ensure its correctness.