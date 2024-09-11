### Concatenating a List of Strings

#### Problem Statement

Write a Python function `concatenate(strings: List[str]) -> str` that takes a list of strings as input and returns their concatenation as a single string. The function should handle an empty input list and return an empty string in this case.

#### Solution

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: The concatenated string

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Use the join function to concatenate all strings in the list
    # The join function requires an iterable of strings, so we pass the list directly
    # The empty string is used as the separator, effectively concatenating the strings without any separation
    return ''.join(strings)
```

You can test this function with the provided example inputs using the example code:

```python
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This function works by passing the list of strings to the `join` function, which concatenates all strings in the list without any separator (since an empty string is used as the separator). The result is returned as the concatenated string.