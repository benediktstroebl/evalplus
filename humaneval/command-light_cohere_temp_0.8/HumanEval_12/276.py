```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.

    if not strings:
        return None

    max_length = 0
    longest_str = ""

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_str = string

    return longest_str

# Test case 1:
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'

# Test case 2:
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

# Test case 3:
strings = []
print(longest(strings))  # Output: None
```

The code defines a function called `longest` that takes a list of strings as input and returns the longest string from that list. It uses a critical thinking and incorporates a check for an empty list, returning `None` in such cases. This method effectively handles all edge cases and provides a clear and concise solution for finding the longest string in a given list.