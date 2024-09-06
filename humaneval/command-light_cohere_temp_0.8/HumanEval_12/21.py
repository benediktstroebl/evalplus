```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from a list of strings.
    Args: strings (list of strings) 
    Returns: The longest string, or None if empty list.
    """
    def find_longest(self):
        # use max with None as initial value, so that empty list will return None
        return max(strings, None)
```