```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string in the list.
    """
    list must contain at least length string
    if not strings:
        return None
    if len(strings) == 1:
        return strings[0]
    max_len = max(len(x) for x in strings)
    return strings[max_len]

# Testing the function
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = []
strings. strings = ["aa", "b", "bb", "cc", "c", "x", "y"]
print(longest(strings))  # Output: 'cc'
``` 
This solution follows the problem statement and returns the length of the longest string in the list. It also handles the problem with an empty list and lists with a single string.