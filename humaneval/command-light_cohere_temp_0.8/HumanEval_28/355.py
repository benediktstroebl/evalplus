```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)

# Tests
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result == 'abc')  # True
strings = []
result = concatenate(strings)
print(result == '')  # True
``` 
This Python code provides a self-contained solution and test for the problem you initially asked.  The code defines the concatenate function that takes a list of strings as an argument and returns the concatenated string. This is string is built by using the join method on the strings list.