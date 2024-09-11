### Concatenate List of Strings into a Single String

Below is a Python script that defines the `concatenate` function to join a list of strings into a single string.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the concatenation of all strings in the input list.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello','', 'world']))  # Output: 'hello world'
```

This script defines the `concatenate` function that uses the `join` method of the `str` class to concatenate the strings in the input list. The `join` method returns a string concatenated with the elements of an iterable. In this case, we pass an empty string (`''`) to the `join` method to concatenate the strings without any separator.