```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```

This Python script defines a function called `longest` that takes a list of strings as input. If the list of strings is empty, the function returns `None`. If there's only one string in the list, the function returns the only string. If there are multiple strings, the function returns the longest one using the `max` function and a custom key function that determines the maximum string length. This approach ensures that the function handles various scenarios and returns the longest non-empty string from the list.