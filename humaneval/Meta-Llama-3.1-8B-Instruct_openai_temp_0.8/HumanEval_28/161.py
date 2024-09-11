### Concatenating a List of Strings

Here's a Python function that concatenates a list of strings into a single string.

```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: Concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Example usage:
if __name__ == "__main__":
    print(concatenate(["Hello", ", ", "world", "!"]))  # Output: Hello, world!
```

This `concatenate` function takes a list of strings as input and uses Python's built-in `join` method to concatenate them. The `join` method takes an iterable of strings and concatenates them with the string it's called on in between each pair of strings. Since we want to concatenate the strings without any separator, we call `join` on an empty string (`''`).