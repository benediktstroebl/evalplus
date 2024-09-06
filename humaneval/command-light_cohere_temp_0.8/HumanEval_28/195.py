```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of string
    Returns:
        str: concatenated string
    """
    return ''.join(strings)

# Test case 1
strings = [""]
result = concatenate(strings)
print(result)  # Output: ""

# Test case 2
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: "abc"

# Test case 3
strings = []
result = concatenate(strings)
print(result)  # Output: ""

# Test case 4
strings = ["a", "b", "c"]
result = concatenate(["xx", "y"])
print(result)  # Output: "axy"
```
The provided code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string, returning the result.

The code also provides a series of test cases to verify the correctness of the `concatenate` function.