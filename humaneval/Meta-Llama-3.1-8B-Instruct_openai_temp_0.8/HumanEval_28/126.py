### Concatenating a List of Strings into a Single String

Here is a Python script that uses the `join()` method to concatenate a list of strings into a single string:

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
    strings (List[str]): A list of strings to be concatenated.

    Returns:
    str: A single string that is the result of concatenating all strings in the input list.

    Example:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

In this script, the `concatenate()` function uses the `join()` method to concatenate all strings in the input list into a single string. The `join()` method takes an iterable (in this case, the input list) and concatenates all its elements into a single string. The `''` argument to the `join()` method specifies that the strings should be joined with no separator.