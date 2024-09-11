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
    # Use the join() method to concatenate all strings in the list
    # The join() method takes an iterable of strings and concatenates them
    # with the string it's called on in between each pair of strings
    # Since we want to concatenate the strings without any separator, we call join() on an empty string
    return ''.join(strings)


# Test the function
print(concatenate([]))  # Expected output: ''
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
```

This script defines a function `concatenate()` that takes a list of strings as input and returns their concatenation. The function uses the `join()` method to concatenate the strings. The script also includes example use cases to demonstrate how to use the function.