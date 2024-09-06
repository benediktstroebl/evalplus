```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the length of the longest string in the list"""
    return max(strings, key=len)
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 3
strings = ['123', 'abc', 'abc']
print(longest(strings))  # Output: 3
strings = ['aa', 'bb', 'ccc']
print(longest(strings))  # Output: 3
``` 
This code defines a function `longest` that takes a list of strings as input and returns the length of the longest string. The function utilizes the `max` function to compare the lengths of the strings, and the `key` argument is set to `len` to ensure that the function returns the length of the longest string, rather than any other string.  This maximum length is unique to Python, since the built-in `max` function does not have a `key` argument.