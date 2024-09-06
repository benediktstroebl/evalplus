Here's the Python script that provides a self-contained function `longest()` to find the longest string in an input list of strings:

```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Finds the length of the longest string in the input list.
    """
    return max(len(x) for x in strings)
```

This code defines a function `longest` that takes a list of strings as input and returns the length of the longest string in the list. The `max()` function is used to find the length of the longest string, and the `len()` function is used to get the length of each string in the input list.