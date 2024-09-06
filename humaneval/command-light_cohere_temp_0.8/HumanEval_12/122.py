```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    if not strings:
        return None
    
    max_len = 0
    max_str = ""
    for str in strings:
        if len(str) > max_len:
            max_len = len(str)
            max_str = str
    return max_str

# Test cases
print(longest(['a', 'b', 'c'])) # Output: 'a'
print(longest(['aa', 'bb', 'ccc'])) # Output: 'ccc'
print(longest(['abrc', 'foo', 'abc'])) # Output: 'abc'
print(longest([])) # Output: None
```