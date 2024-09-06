Here's the self-contained Python script that defines a function `longest()` to return the longest string from a list of strings:

```python
from typing import List

def longest(strings: List[str]) ->:
    """ Out of list of strings, returns the longest one
        """
    return max(strings, key=len) if strings else None

# Test cases
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest:", longest_result)

strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest:", longest_result)

strings = []
strings. longest
longest_result = longest(strings)
print("Longest:", longest_result)
```

This function `longest()` takes a list of strings and returns the longest string using the `max()` function, passing `len` as the key. It also has a specific test case to check if the input list is empty.