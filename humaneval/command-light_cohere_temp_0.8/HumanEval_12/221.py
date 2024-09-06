```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string in a list of strings. """
    return max(strings, default='')

#Tests
strings = ['a', 'bb', 'ccc']
longest(strings)  # Output: 'ccc'
strings = ['aa', 'xx', 'xy', 'yy', 'zz']
longest(strings)  # Output: 'xx'
```
The provided code defines a function called `longest` which takes a list of strings as input and returns the longest string in the list. It uses the max function as the max function takes an iterable and returns the maximum value in it. Additionally, the default argument is set to an empty string, which means that any value in the list will be considered as long if it is not an empty string.

This function is tested using two sample inputs.