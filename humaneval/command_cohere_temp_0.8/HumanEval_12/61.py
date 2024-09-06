Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(longest_string) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_string]
    )
```

This script defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function first finds the longest string in the list using the `max` function with the `key` argument set to the length of the string. If there are multiple strings of the same length, the function removes all but the first from the list, and recursively calls itself on the filtered list, ensuring that the result is the first string of any length. Would you like to know more about any of the methods used in this code?