```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the longest string from the list of strings.
    """
    returns the particular string with the maximum length
    """
    if not strings:
        return None
    return max(strings, key=len)
# Example test cases
strings = ["a", "bb", "ccc"]
longest_res = longest(strings)
print(longest_res)  # Output: 'ccc'
``` 
This code implements the `longest()` function, which takes a list of strings as input and returns the longest string from that list. It uses the max() function with the `key=len` argument to find the string with the maximum length. It is also handle the empty list case, where it returns `None`.