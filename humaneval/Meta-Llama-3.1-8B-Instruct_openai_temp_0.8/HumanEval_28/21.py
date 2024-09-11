```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
    strings (List[str]): A list of strings to be concatenated

    Returns:
    str: The concatenated string

    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Use the join method of the string class to concatenate the list of strings
    # The join method takes an iterable of strings and concatenates them with the string it's called on in between each string
    # Since we want to concatenate the strings without any separator, we call the join method on an empty string
    return ''.join(strings)


# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```