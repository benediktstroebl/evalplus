```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one.
    """
    first = strings[0]
    if len(strings) == 0:
        return None
    else:
        for string in strings:
            if len(string) > len(first):
                first = string
    return first

# Test the function
print(longest(['a', 'bb', 'ccc']))
```