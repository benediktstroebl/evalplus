```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from a list of strings.
    :Return the string if all strings are of the same length
    """
    if not strings:
        return None
    return max(strings, key=len)

# Example test cases
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 'ccc'

strings = ["a"]
print(longest(strings))  # Output: 'a'

strings = ["adf", "aces", "acadf"]
print(longest(strings))  # Output: 'aces'

strings = []
print(longest(strings))  # Output: None
```