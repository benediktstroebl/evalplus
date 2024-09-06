```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate

    Returns:
    str: Concatenated string
    """
    return ''.join(strings)

# Example test cases
strings = ["a", "bc", "xyz", "f"]
result = concatenate(strings)
print(result)  # Output: abcxyzf

strings = []
result = concatenate(strings)
print(result)  # Output: 

strings = ["a", "bc"]
result = concatenate(strings)
print(result)  # Output: abc
```