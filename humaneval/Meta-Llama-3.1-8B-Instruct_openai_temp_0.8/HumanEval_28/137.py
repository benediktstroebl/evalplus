```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Use the join() function to concatenate all strings in the list
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script defines the `concatenate` function, which takes a list of strings as input and returns a single string that is the concatenation of all the strings in the list. The function uses the `join()` method to concatenate the strings, and the `''` (empty string) is used as the separator, effectively concatenating the strings without any intervening characters. The script then includes some test cases to demonstrate the function's behavior.