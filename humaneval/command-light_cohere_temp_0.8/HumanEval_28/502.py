```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)
# Create a list of strings
strings = ["a", "b", "c"]
# Test the function
print(concatenate(strings))  # Output: abc
```