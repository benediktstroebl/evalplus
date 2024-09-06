```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join() + ''.join(strings)
input_strings = ['a', 'b', 'c']
print(concatenate(input_strings))  # Output: 'abc'
input_empty = []
print(concatenate(input_empty))  # Output: ''
input_single = ['a']
print(concatenate(input_single))  # Output: 'a'
```
This function concatenates a list of strings into a single string, using the technique of string concatenation with backslashes.