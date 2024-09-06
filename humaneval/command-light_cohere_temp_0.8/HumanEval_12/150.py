Here is a Python script that passes the test cases you provided:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list of strings.
    """
    return max(strings, key=len)
# Test cases
test_strings = ['a', 'bb', 'ccc']
longest_result = longest(test_strings)
assert longest_result == 'ccc'
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string from that list. The `max` function is used to find the maximum length of the strings in the list, and the `key=len` argument is used to make the length the key for the maximum. 

Then the test cases are defined to verify that the function works correctly.