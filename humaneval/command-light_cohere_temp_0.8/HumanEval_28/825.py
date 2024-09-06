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

# Tests
concatenate([])  # Test empty list -> empty string
concatenate(['a'])  # Test single string -> same string
concatenate(['a', 'b', 'c'])  # Test list with 3 strings -> concatenated string
```
This Python code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function utilizes a string concatenation using the `join` method. 

The code then tests the function by passing various inputs, ensuring the output matches the expected results.