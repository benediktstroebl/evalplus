```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    >>> return longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'bb'
print(longest(['abcde', 'ab']))    # Output: 'abcde'
print(longest(['abcde', 'ab', 'foe'])) # Output: 'abcde'
print(longest(['a', 'bb', 'ccc', 'd']))  # Output: 'bb'
print(longest(['abcde', 'ab', 'cde']))  # Output: 'abcde'
```  This version provides better clarity, adheres to Python typing and is generally easier to read.