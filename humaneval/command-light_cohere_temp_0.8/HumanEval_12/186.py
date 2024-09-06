```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one, or None if empty """
    if not strings:
        return None
    return max(strings, key=len)

# Sample test case
test_strings = ['a', 'bb', 'ccc']
longest(test_strings)  # Output: 'ccc'
test_empty = []
longest(test_empty)  # Output: None
test_single = 'a'
longest(test_single)  # Output: 'a'
```