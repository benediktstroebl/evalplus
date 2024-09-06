Here is a self-contained Python script that defines a function to find the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from the list.
    """
    return max(strings, key=len)
```

This function takes a list of strings as input and returns the longest string in that list. It does so using the by using the `max()` function along with the `key=len` argument, which tells Python to return the element with the longest index.