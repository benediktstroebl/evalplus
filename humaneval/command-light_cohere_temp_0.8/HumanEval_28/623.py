```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate 
    Returns:
        concatenated string
    """
    assert len(strings) > 0, "Input list cannot be empty"
    return ''.join(*strings)

# Example usage
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result) # Output: abc
```