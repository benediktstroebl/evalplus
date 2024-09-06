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

This code defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If there are multiple strings of the same length, it returns the first one. If the list is empty, it returns `None`. The logic of the function is straightforward: it checks if the list is empty, and since it's impossible to have a longest string among an empty list, it returns `None`. In the other two cases, it returns the longest string, using the `max` function to compare the strings by their length as a key.

This solution is efficient and straightforward, providing a clear and reusable implementation that solves the problem.