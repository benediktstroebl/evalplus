### Concatenating List of Strings into a Single String

Here's a Python function that takes a list of strings and returns a single concatenated string.

```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single concatenated string

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)
```

This code defines a function `concatenate` that takes a list of strings `strings`. It uses the built-in string method `join()` to concatenate all the strings in the list into a single string. If the input list is empty, it returns an empty string.

You can use this function like this:
```python
strings = ['Hello', 'world!', 'This', 'is', 'a', 'test.']
result = concatenate(strings)
print(result)  # Output: 'Hello world!This is a test.'
```