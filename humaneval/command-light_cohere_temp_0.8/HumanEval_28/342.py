Sure, here's a self-contained Python script that implements the `concatenate` function to join a list of strings into a single string:

```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

strings = []
result = concatenate(strings)
assert result == ""
```

This script defines a `concatenate` function that takes a list of strings as an argument and returns the concatenated string. The test cases are also provided to the function, which successfully passes.