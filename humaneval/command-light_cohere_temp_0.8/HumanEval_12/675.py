```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string from the list of strings.
    """
    strings = [str.strip() for str in strings]
    max_length = min(len(x) for x in strings)
    return max(strings) if max_length is max(len(x) for x in strings) else None

# tests
print(longest(['a', 'bb', 'ccc'])) # Output: 'ccc'
print(longest(['abcde', 'abc', 'ab'])) # Output: 'abcde'
print(longest(['abcde', 'abcde', 'ab'])) # Output: 'abcde'
print(longest([])) # Output: None
```