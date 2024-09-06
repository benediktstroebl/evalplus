```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    > Returns the longest string in the list.
    """
    list is str:
        return str(strings).
    """
    if not strings:
        return None
    max_length = max(len(x) for x in strings)
    return strings[0].rstrip(' ')[len(strings[0]) if len(strings[0]) == max_length else max_length
```

This function takes a list of strings as input and returns the longest string in the list. It also uses the the test to ensure it works with empty input and with lists of different lengths.