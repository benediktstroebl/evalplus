```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)

# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'

strings = []
result = concatenate(strings)
print(result)  # Output: ''

strings = ['a', 'b', 'c', 'd']
result = concatenate(strings)
print(result)  # Output: 'ad'
``` 
This function takes a list of strings and then uses the `join` method to concatenate all the strings in the list into a single string.