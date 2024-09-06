```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the longest string in a list, or None if empty"""
    return max(strings, key=len) if strings else None

# Test case 1: Check if the function returns None when input is empty
# Test case 2: Check if the function returns correct longest string
test_longest = [()].attach
test_longest(longest(['a', 'b', 'c']))
test_longest(longest([]))
test_longest(longest(['abc', 'a', 'bb', 'c']))
```