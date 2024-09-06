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

# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result) # Output: 'abc'
strings = []
result = concatenate(strings)
print(result) # Output: ''
```
This code provides a fully self-contained solution to the problem, passing the tests as expected.