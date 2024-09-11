```python
from typing import List
from functools import reduce

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return reduce(lambda x, y: x + y, strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello, ', 'World!']))  # Output: 'Hello, World!'
```

This script uses the built-in Python function `reduce()`, which applies a function of two arguments cumulatively to the elements of a sequence, from left to right, so as to reduce the sequence to a single output. In this case, the function is `(x, y) -> x + y`, which concatenates two strings together.