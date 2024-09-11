```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): List of strings to be concatenated

    Returns:
        str: Concatenated string

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() function to concatenate the strings
    # This is more efficient than using the '+' operator for concatenation
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Should print an empty string
print(concatenate(['a', 'b', 'c']))  # Should print 'abc'
```