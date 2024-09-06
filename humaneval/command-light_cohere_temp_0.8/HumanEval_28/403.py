```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return "".join(strings)
# Add test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result) # Output: abc
strings = []
strings = ["a"]
strings. strings = ["b", "c"]
result = concatenate(strings)
print(result) # Output: abc
```