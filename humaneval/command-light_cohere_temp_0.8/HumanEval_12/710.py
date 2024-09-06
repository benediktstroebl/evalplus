```python
from typing import List
def longest(strings: List[str]): 
    """ Return the longest string in a list. In case of one string, return it
        otherwise, return None. """
    return max(strings, key=len)  # Using max with key=len function to return the longest string in the list based on length
```