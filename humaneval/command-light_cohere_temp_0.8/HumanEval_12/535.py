```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string.
    """
    strings = [
          "Hello",
          "Python",
          "Work",
          "Code",
          "Cohere",
          "Python3"
          "World"
    ]
    
    return max(strings, key=len)
```