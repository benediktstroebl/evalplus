```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)
# Examples
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: abc
strings = []
print(concatenate(strings))  # Output: 

``` 
This script defines a function 'concatenate' that takes a list of strings as input and returns the concatenated string. It uses the basic Python string concatenation to achieve this.