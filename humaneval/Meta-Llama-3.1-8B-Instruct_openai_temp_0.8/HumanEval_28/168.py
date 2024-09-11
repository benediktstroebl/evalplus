```python
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): A list of strings to concatenate.
    
    Returns:
        str: The concatenated string.
    
    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)


# Test the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello, ', 'World!']))  # Output: 'Hello, World!'
```

This script defines the `concatenate` function as specified, and includes two test cases in the `if __name__ == "__main__":` block to demonstrate its usage.