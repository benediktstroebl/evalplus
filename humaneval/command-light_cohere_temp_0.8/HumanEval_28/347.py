```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        joined string
    """
    return "".join(strings)
# Test the function
print(concatenate(['a', 'b', 'c'])) # Output: 'abc'
print(concatenate([''])       ) # Output: ''
print(concatenate(['a', 'xx', 'c'])) # Should raise an error
```