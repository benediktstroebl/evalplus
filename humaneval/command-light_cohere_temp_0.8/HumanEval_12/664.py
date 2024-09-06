```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    #Check if the list is empty
    if not strings:
        return None
    #Find the longest string in the list
    longest_string = max(strings, key=len)
    return longest_string
```