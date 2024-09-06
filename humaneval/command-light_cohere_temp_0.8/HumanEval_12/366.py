```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> strings = ['a', 'bb', 'ccc']
    return max(strings, key=len)
    """
    return max(strings, key=len)

# Test cases
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: "ccc"

strings = ['apple', 'a', 'bed']
strings. longest = 10
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: "bed"

strings = []
strings. empty[1:3] = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest string:", longest_result) # Output: "ccc"
```
The function `longest()` takes a list of strings as input and returns the longest string in the list. The function uses the max() function with the key argument set to `len` to sort the strings in ascending order based on their length, and then returns the first string that matches the length of the maximum length.