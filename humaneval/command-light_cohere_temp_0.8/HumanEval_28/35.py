```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(''.join(strings))
# Test the function
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
``` 
This code provides a self-contained function 'concatenate' that takes a list of strings as an argument and returns the concatenated string as a result. 
The provided test strings are concatenated successfully.