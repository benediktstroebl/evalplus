```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from the list.
    """
    first_length = 0
    longest_str = ""
    for string in strings:
        if len(string) > first_length:
            first_length = len(string)
            longest_str = string
    return longest_str if longest_str else None

# Example usage
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print(longest_result)  # Output: 'c'
```