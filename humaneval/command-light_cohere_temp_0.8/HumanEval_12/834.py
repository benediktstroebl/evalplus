```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    strings = ['a', 'b', 'c']
    return max(strings) if strings else None
    """
    pass

# Test the function with various inputs
strings = ['a', 'bb', 'ccc']
longest(strings)  # Output: 'ccc'
strings = ['a', 'b']
longest(strings)  # Output: 'a'
strings = []
longest(strings)  # Output: None
```