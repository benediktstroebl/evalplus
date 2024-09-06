```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenentated string
    """
    return "".join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

strings = []
result = concatenate(strings)
assert result == ""
```
This script defines a function called **concatenate** that takes a list of strings as input and concatenates them into a single string. It uses the string method **join** to concatenate the strings into a single string, and passes the test cases successfully.