```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    
    Args:
        strings (List[str]): A list of strings.
    
    Returns:
        str: A concatenated string.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


if __name__ == "__main__":
    # Testing the function
    print(concatenate([]))  # Expected output: ''
    print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
    print(concatenate(['Hello, ', 'world!']))  # Expected output: 'Hello, world!'
```

This script defines a `concatenate` function that takes a list of strings and returns their concatenation. The function uses the `join` method, which is a common and efficient way to concatenate strings in Python. The script also includes some test cases in the `if __name__ == "__main__":` block to demonstrate the function's usage.