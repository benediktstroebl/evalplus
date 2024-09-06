```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

# Test case with an empty list
result = concatenate([])
assert result == ""
```
The solution is a simple list comprehension in the function that joins the strings with ''