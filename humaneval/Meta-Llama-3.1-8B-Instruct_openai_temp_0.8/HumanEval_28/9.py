### Concatenating a List of Strings
#### Using Python's Built-in `join()` Function

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to concatenate.

    Returns:
        str: A single string containing all elements from the input list.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Example usage
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['Hello','', 'World!']))  # Output: 'Hello World!'
```

This script uses Python's built-in `join()` function, which concatenates all elements in the input list into a single string. Since we're joining strings with no separator, passing an empty string (`''`) to `join()` achieves the desired result.