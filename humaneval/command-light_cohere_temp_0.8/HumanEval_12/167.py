```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list.
    """
    list contains any string, None or other type: raise ValueError("Input list must contain only strings")

    return max(strings, key=len)

# Test case:
strings = ['a', 'bb', 'ccc']
longest(strings)
```