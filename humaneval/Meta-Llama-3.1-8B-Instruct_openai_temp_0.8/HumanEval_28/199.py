```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenates list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string created by concatenating all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test the function
if __name__ == "__main__":
    print(concatenate([]))  # Should print: ''
    print(concatenate(['a', 'b', 'c']))  # Should print: 'abc'
    print(concatenate(['Hello','', 'World!']))  # Should print: 'Hello World!'
```

This script uses the `join()` method to concatenate all the strings in the input list. The `join()` method returns a string by concatenating all the strings in the input list, separating them by a string specified as its argument. In this case, we use an empty string as the argument to concatenate the strings without any separator.