```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list. string, case insensitive matching.
    """
    Takes a list of strings as input and returns the longest string.
    """
    matching is case insensitive, so we convert to lowercase before comparison
    """
    if not strings:
        return None
    return max(strings.lower(), key=len)
```
This function takes a list of strings as input and returns the longest string. It uses the max function to get the maximum value of a given property of each string in the list, and the property is the lowercase version of the string.