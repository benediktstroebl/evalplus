Here is a Python script with a self-contained function that solves the problem of concatenating a list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings
    :return: string
    """
    return ''.join(strings)
# Test the function with various inputs
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
strings = ['a', 'b', 'ccc']
print(concatenate(strings))  # Output: 'bccc'
strings = ['a', 'bc', '']
print(concatenate(strings))  # Output: 'abc '
``` 
This function takes a list of strings as input and concatenates them into a single string. It uses the string. This is output the process with a function call.