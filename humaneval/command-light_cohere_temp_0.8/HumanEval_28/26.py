```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return "".join("".join(strings))
# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

strings = []
result = concatenate(strings)
assert result == ""

strings = ["a", "bc", "d"]
result = concatenate(strings)
assert result == "abcd"
```
This script defines a function `concatenate` that takes a list of strings as input and returns the concatenated string. The test cases ensure the using sample inputs and assert the expected output.