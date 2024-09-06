```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list of strings.
    """
    # Validate input
    If input list is empty, return None
    """
    if not strings:
        return None

    # Sort the strings
    strings.sort()

    # Return the least
    """
        return strings[0]
    """

# Unit tests
strings = ['a', 'b', 'c']
longest_res = longest(strings)
print(longest_res)  # Output: c

strings = ['aa', 'bb', 'ccc']
longest_res = longest(strings)
print(longest_res)  # Output: bb

strings = ['abc']
longest_res = longest([str])
print(longest_res)  # Output: abc
```
This Python script defines a function `longest` that takes a list of strings as input and returns the longest string. It also includes unit tests to validate the function's behavior.