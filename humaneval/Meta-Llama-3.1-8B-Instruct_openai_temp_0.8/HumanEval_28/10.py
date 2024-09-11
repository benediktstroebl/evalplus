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
    # Use the join() method to concatenate all strings in the list
    # The join() method returns a string concatenated with the elements of an iterable
    # In this case, we use an empty string as the separator
    return ''.join(strings)

# Test the function
print(concatenate([]))  # Should print an empty string
print(concatenate(['a', 'b', 'c']))  # Should print 'abc'
```