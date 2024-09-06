```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    """
    # Convert the out input list of strings to a list of characters
    all = ''.join(x for x in strings if x not in all)
    all.length = len(all)

    # If length is 0 or empty, the list is empty
    if length <= 0:
        return None

    # Return the longest string in the list of characters
    return all[-length:]
```