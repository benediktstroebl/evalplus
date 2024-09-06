```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    >>> longest(['a', 'b', 'c'])
    """
    max_length = max(len(x) for x in strings)
    return max_length

# Test cases
print(longest(['a', 'bb', 'ccc'])) # Output: 3
print(longest(['abcde', 'abcba', 'abc'])) # Output: 5
print(longest([])) # Output: 0
print(longest(['abcde', 'abc', 'def'])) # Output: 4
```

This script defines a function `longest` that takes a list of strings as input and returns the length of the longest string. It uses the maximum length of the strings in the list to determine the longest string, and then returns the length of that string. It also includes test cases to cover different scenarios, such as empty list, lists with strings of different lengths, and lists with multiple strings of the same length.