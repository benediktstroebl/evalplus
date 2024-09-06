```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    """
    max_length = len(strings[0])
    for string in strings[1:]:
        if len(string) > max_length:
            max_length = len(string)
    return max_length if max_length is not None else None

# Test the function
print(longest(['a', 'bb', 'ccc']))  # Output: 3
print(longest(['abcde', 'abcba', 'ac']))  # Output: 3
print(longest(['abcde', 'abcdab', 'ab']))  # Output: 2
print(longest(['abcde', 'abcd', 'abcda']))  # Output: 3
```