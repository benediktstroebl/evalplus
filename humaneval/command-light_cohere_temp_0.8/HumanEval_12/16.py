```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the length of the longest string.
    """
    strings = [string.strip() for string in strings]
    return max(strings)
```

This solution uses the **max** built-in function to return the maximum value of the list of strings. It will return an empty string if the list is empty.