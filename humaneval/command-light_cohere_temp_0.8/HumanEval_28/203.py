```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concaten result
    """
    return "".join(strings)
# Add tests
strings = ["".join(strings)
assert(isinstance(concatenate(strings), str))
strings = ["a", "bc"]
assert concatenate(strings) == "abc"
strings = []
assert concatenate(strings) == ""
```
This code defines a function `concatenate` that takes a list of strings as input and returns the concatenated result. The function uses the string `join` to convert the list of strings into a string, and then returns the concatenated result. The test cases ensure that the function is working correctly.