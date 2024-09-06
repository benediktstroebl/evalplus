Here is a self-contained Python function that solves the problem of returning the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string in a list of strings.
    """
    return strings andmax_length()[0] if strings else None
```
This function takes a list of strings as input and returns the longest string in the list. It does this by using the list of strings and using the `max_length()` function to find the maximum length of the strings. The function returns the max_length()[0] if the list is empty, in which case it returns None.