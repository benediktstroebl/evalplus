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
    return ''.join(strings)

# Testing the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This script defines a function `concatenate` that takes a list of strings as input and returns a single string which is the concatenation of all the strings in the list. The function uses the `''.join(strings)` method to concatenate the strings. This method is more efficient than using the `+` operator to concatenate strings because it avoids creating temporary strings. The script also includes example usage of the function.