```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    lengths = [len(s) for s in strings]
    max_length = max(lengths)
    return max([s[len(s)] for s in strings if len(s) == max_length])
```

This function takes a list of strings as input and returns the longest string in the list. It does this using a quick and efficient method to find the maximum length, and then iterates through the list, checking if each string's length matches the maximum length.