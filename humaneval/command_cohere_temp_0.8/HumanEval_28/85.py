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
The function concatenate takes a list of strings, iterates through them, and appends each string to a string concatenated_strings. Ultimately, it returns the final concatenated_strings string. 

This approach results in a clean and concise solution that solves the problem and retains clarity for future coders to understand. 

The tests for this function can be run by importing the function concatenate into a Python interpreter and calling it with the desired input, which should return the expected output.