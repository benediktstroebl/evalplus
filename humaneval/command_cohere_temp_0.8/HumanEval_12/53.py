```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(longest_string) == max(len(s) for s in strings) else longest(
        [s for s in strings if s != longest_string]
    )
``` 

This code uses `max` with a custom key to identify the longest string, and then recursively searches for the longest string among the rest if the longest is not unique in terms of length. This will ensure the function returns the single longest string among those of equal length.