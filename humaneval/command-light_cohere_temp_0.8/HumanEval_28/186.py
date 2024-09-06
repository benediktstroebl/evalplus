```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate  
    Returns:
        single string combining all input strings
    """
    return ''.join(strings)

#Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: abc
strings = []
result = concatenate(strings)
print(result)  # Output: 

strings = ["a", "!"]
result = concatenate(strings)
print(result)  # Output: !abc
```