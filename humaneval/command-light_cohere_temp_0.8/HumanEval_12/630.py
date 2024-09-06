```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    if not strings:
        return None
    max_len = max(len(str) for str in strings)
    return str(max_len)

# Test the function
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: c
```