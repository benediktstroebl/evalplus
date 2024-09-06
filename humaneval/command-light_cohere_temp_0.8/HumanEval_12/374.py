Here's a self-contained Python script that defines a function `longest()` that correctly identifies the longest string from a list of strings:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Find the length of the longest string in the list.
    Args:
        strings: list of strings
    Returns:
        longest string or None if empty list
    """
    if not strings:
        return None
    
    max_len = max(map(len, strings))
    longest_string = strings[0]
    for string in strings:
        if len(string) == max_len:
            longest_string = string
    
    return longest_string
```

This code takes a list of strings as input and returns the longest string from that list. It works for both empty list as well. This approach is using the map to find the max length and then take the first string that matches the length as the longest one.