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
    # Use the join() method to concatenate the strings
    # The join() method takes an iterable of strings and concatenates them with the string it's called on in between each pair of strings
    # Since we want no separation between the strings, we call join() on an empty string
    return ''.join(strings)


# Test the function
print(concatenate([]))  # Should print an empty string
print(concatenate(['a', 'b', 'c']))  # Should print 'abc'
```

This script defines a function `concatenate` that takes a list of strings and returns a single string that is the concatenation of all the strings in the list. The `join` method is used to concatenate the strings. The function is then tested with two examples: an empty list and a non-empty list.