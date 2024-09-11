```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string
    """
    # Using the built-in join function to concatenate the strings
    # The join function takes an iterable of strings and concatenates them
    # The empty string '' is used as the separator, implying no separator
    return ''.join(strings)

# Test the function with some examples
print(concatenate([]))   # Expected output: ''
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
print(concatenate(['Hello, ', 'world!']))  # Expected output: 'Hello, world!'
```

This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. It uses the built-in `join` function to concatenate the strings, which is a more efficient and Pythonic way to do it. The script also includes some test cases to demonstrate the function's behavior.