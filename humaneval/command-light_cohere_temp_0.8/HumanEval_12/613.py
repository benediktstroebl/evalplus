```python
from typing import List
def longest(strings: List[str]):
    # Checks if input list is empty
    if not strings:
        return None
    # Finds the length of each string in the list
    lengths = [len(string) for string in strings]
    # Sorts the list of lengths based on the length of each string
    sorted_lengths = sorted(lengths)
    # Returns the first element of the sorted list
    return sorted_lengths[0] if sorted_lengths else None
```
This code defines a function called **longest** that takes a list of strings as input and returns the length of the longest string in the list.