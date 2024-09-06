Here's the code:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    Args:
        strings (List[str]): A list of strings.
    Returns: the longest string in the list.
    """
    return max(strings, default='')
```

This script defines a function called `longest` that takes a list of strings as input and returns the longest string in that list. The function uses the max function to find the maximum value of a given list, and uses the default argument to ensure the function works correctly with empty input lists.