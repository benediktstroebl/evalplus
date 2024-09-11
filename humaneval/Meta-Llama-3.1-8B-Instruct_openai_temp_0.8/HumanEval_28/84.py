```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string resulting from concatenating all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))   # Expected output: ''
print(concatenate(['a', 'b', 'c']))   # Expected output: 'abc'
print(concatenate(['hello','', 'world']))   # Expected output: 'hello world'
```

This Python script defines a function `concatenate` that takes a list of strings as input and returns a single string resulting from concatenating all input strings. The function uses the `join` method of the string class, which concatenates all elements in the list into a single string. The script also includes example use cases to demonstrate the function's behavior.