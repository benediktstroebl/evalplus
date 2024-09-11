```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenates a list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to concatenate.

    Returns:
        str: A single string containing all the input strings.
    """
    # Use the join method of the empty string to concatenate all strings in the list
    return ''.join(strings)

# Test cases
print(concatenate([]))  # Expected output: ''
print(concatenate(['a', 'b', 'c']))  # Expected output: 'abc'
```