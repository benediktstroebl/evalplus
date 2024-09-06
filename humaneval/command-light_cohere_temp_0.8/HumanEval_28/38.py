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

# Test case 1: empty list
print(concatenate([]))  # Output: empty string

# Test case 2: single string
print(concatenate('a'))  # Output: 'a'

# Test case 3: two strings
print(concatenate(['a', 'b']))  # Output: 'ab'

# Test case 4: list of strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The test cases provided at the time demonstrate the usage of the function. The output for each cases matches the expected result.