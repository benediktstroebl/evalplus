```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return "".join(strings)
# Test the function with various inputs
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  
# Output: abc
strings = [""]
result = concatenate(strings)
print(result)  
# Output: 

strings = ["a", "b", "c", "d"]
result = concatenate(strings)
print(result)  
# Output: abcdd
```