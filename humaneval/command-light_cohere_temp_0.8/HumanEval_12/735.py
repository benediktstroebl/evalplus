```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string in the list.
    """
    list must only contain one or more strings of the same length to work.
    """
    return max(len(string) for string in strings)
```
This function takes a list of strings as input and returns the length of the longest string in the list. It uses the max function to get the length of the longest string and returns that length.