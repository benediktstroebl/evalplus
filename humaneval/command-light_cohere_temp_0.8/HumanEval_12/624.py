```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string from a list of strings. """
    longest = [s.join() for s in strings if len(s) > len(max_) else max_

    return max_

# Test cases
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 'ccc'
strings = []
strings. strings = [1, '1', 3]
print(longest(strings))  # Output: '1'
strings = ["abc", "abc", "abc"]
print(longest(strings))  # Output: 'abc'
```

This solution defines a function `longest` that takes a list of strings as input and returns the longest string from that list. It uses a string length comparison to determine which string is longer, and then returns that string.