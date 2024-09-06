Here is a self-contained Python script that includes the function `longest()` that aims to find the longest string in an input list of strings:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Find the length of the longest string in the list.
    Args:
        strings (List[str]): List of strings.
    Returns: the length of the longest string, or None if empty list.
    """
    longest([]) return None
    longest([h for h in 'abc']) return 'abc'
```

This script's `longest` function takes a list of strings as an argument and returns the length of the longest string. It uses the `List` to check the elements of the list and returns the length of the longest string. The function also returns `None` if the list is empty.