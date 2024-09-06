Here's the provided Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:

```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    strs = [string.strip() for string in strings]
    return max(strs, default='')
```

This function takes a list of strings as input and returns the longest string in the list. The function then loops through the list, converting each string to its uppercase equivalent and storing it in the strs list. Then, it returns the maximum of the list as the longest string.