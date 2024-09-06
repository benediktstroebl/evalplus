Here's a self-contained Python script that provides a function to find the longest string in a list:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
   :
        if not strings:
            return None
        return max(strings, key=len)
```
This script has a single function, `longest`, which takes a list of strings as an argument and returns the longest string in that list. The function uses the maximum function with the `len` key to find the longest string in the list.