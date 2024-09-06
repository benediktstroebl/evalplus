```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """

    strings = [sub(' ', '') for sub in strings]  # Convert to lowercase and remove spaces
    return max(strings, key=len)
```