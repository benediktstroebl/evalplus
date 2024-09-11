```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello, World!']))  # Output: 'Hello, World!'
print(concatenate(['This', 'is', 'a', 'test']))  # Output: 'Thisisatest'
```

In this script, I've implemented the `concatenate` function as requested. The function uses the `join` method of a string to concatenate all the strings in the input list together. If the input list is empty, an empty string is returned. I've also added some test cases at the end to demonstrate the function's behavior.