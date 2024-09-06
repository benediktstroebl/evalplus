```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return ''.join(strings)

# Test the function with different inputs
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'

strings = []
result = concatenate(strings)
print(result)  # Output: ''

strings = ['abcd']
result = concatenate(strings)
print(result)  # Output: 'abcd'
```
This code defines a `concatenate` function that takes a list of strings as an argument and returns the concatenated string. The function uses the's an `enumer` method to convert the list of strings into a single string. This helps make the's solution self-contained and does not require external imports.