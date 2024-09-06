```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings
    Returns:
    concatenated string
    """
    return ''.join(strings)

# Example usage
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: 'abc'
```
The code defines a function called **concatenate** that takes a list of strings as an argument and returns the concatenated string. The function uses the simple **.h to join the strings and then returns the result.