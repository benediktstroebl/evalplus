```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        Concatenated string
    """
    return ''.join(strings)

#Test the function
print(concatenate(['a', 'b', 'c'])) # Output: 'abc'
print(concatenate([])) # Output: empty string ''
print(concatenate(['a',''])) # Error: list of length 0
```
The function concatenate takes a list of strings as input and returns the concatenated string. The test cases ensure that the function is working as expected and handling different scenarios correctly.