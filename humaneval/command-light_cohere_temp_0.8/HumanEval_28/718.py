```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: List of strings
    Returns:  str - Concatented string
    """
    return "".join(strings)

# Test the function with various inputs
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

strings = []
result = concatenate(strings)
assert result == ""

strings = ["foo"]
result = concatenate(strings)
assert result == "foo"

strings = ["a", "foo", "bar"]
result = concatenate(strings)
assert result == "foobar"
```
The function concatenate in the provided code takes a list of strings as an argument and returns the concatenated string by using the join() method. The code also provides a test cases to ensure that the function works correctly for various inputs.