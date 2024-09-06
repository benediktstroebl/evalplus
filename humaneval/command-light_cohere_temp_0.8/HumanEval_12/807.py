```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list of strings.
    """
    strings = [str for str in strings if len(str) == len(strings)][0]
    return strings if strings is not None else None

# Unit tests
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest:", longest_result)  # Output: c
```