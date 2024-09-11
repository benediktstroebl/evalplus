```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the result of concatenating all strings in the input list.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Testing the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

In this script, we use the built-in `join()` method of the string class to concatenate the input strings. This method takes an iterable of strings as an argument and returns a single string that is the result of concatenating all strings in the iterable, separated by the string on which the `join()` method is called (in this case, an empty string, which is the default behavior when joining strings).