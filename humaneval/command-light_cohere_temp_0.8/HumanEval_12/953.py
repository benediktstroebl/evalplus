Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    first_length = 0
    longest_str = strings[0]
    for string in strings[1:]:
        if len(string) > first_length:
            first_length = len(string)
            longest_str = string
    return longest_str
```

The function takes a list of strings and returns the longest string. The function compares the string lengths, and the first string with a length greater than the current first_length is updated to the new longest string.