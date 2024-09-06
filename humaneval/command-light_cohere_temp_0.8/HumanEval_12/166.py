```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.

    If empty list, return None
    """

    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest string:", longest_result)  # Output: c

strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest string:", longest_result)  # Output: bb

strings = []
strings. string longest_result = longest(strings)
print("Longest string:", longest_result)  # Output: None
```
This function, `longest`, takes a list of strings as input and returns the longest string in the list. By doing this test if the strings list is empty, the function returns `None`. If the list is not empty, it returns the string with the longest length using the `max` function with the `len` function as the key.