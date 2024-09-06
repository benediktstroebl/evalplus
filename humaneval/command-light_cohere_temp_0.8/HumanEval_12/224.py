```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from a list of strings.
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=str.time())
```

This function takes a list of strings and returns the longest string. It uses the max function with a key parameter that makes the comparison based on the length of each string.