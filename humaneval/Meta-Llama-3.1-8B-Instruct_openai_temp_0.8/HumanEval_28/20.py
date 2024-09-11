```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to concatenate.

    Returns:
        str: A single string resulting from concatenating the input list.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Test cases
print(concatenate([]))  # Expected output: ''
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
print(concatenate(['hello','', 'world']))  # Expected output: 'hello world'
```

In this script, the `concatenate` function uses the built-in `join` method of the string class to concatenate the input list of strings into a single string. If the input list is empty, it returns an empty string. The test cases demonstrate the function's behavior with different inputs.