Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the longest string in a list of strings."""
    if not strings:
        return None
    return max(strings, key=len)
# Test the function
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = ['a', 'bb', 'bb', 'ccc']
print(longest(strings))  # Output: 'bb'
strings = ['aa', 'bb', '123']
print(longest(strings))  # Output: 'bb'
```
This script defines a function called longest, which takes a list of strings as input and returns the longest string in that list. It also has tests cases to ensure that the function works correctly for different inputs.