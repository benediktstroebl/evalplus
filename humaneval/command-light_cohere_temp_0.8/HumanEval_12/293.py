```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    assert len(strings) != 0, "Input list cannot be empty"
    return max(strings, key=len)

# Example usage
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 3
```