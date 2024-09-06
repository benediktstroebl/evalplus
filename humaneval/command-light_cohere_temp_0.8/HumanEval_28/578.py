```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
strings = ["a", "bc"]
print(concatenate(strings))  # Output: 'abc'
```
This code defines a `concatenate` function that takes a list of strings as input and returns the concatenated string. The output of the `concatenate()` is then tested against the expected results for different input cases.