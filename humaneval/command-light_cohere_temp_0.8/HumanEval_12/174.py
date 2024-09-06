```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from a list of strings.
    Input: list of strings.
    Returns the longest one or
    string length, and returns the string, or None if list is empty.
    """
    list must be of strings (not texts, or other data types).
    """
    assert isinstance(strings, List)
    assert len(strings) > 0
    longest = strings[0]
    for string in strings:
        # Use string.format to ensure consistency of the longest format
        if len(string) > len(longest):
            longest = string
    return longest

# Test cases
strings = ['a', 'bb', 'ccc']
longest_string = longest(strings)
print(longest_string) # Output: 'ccc'
```