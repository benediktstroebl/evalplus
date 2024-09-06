```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    longest_length = max(len(s) for s in strings)
    return strings[strings.index(longest_length)]

# Test the function
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest:", longest_result)  # Output: "ccc"
```
This script defines a Python function called `longest` that takes a list of strings as input and returns the longest string from the list. The function first checks if the list is empty, and if so, returns `None`. If the list is not empty, the function finds the index of the longest string using the `max` function and returns the corresponding string.