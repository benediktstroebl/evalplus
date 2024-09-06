Here is a Python script with a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string in the list of strings.
    Args:
    strings: list of strings
    Returns:
    The longest string in the list
    """
    return max(strings, key=len)
# Test case 1
strings = ['a', 'b', 'c']
longest(strings) # Output: 'a'
# Test case 2
strings = ['a', 'bb', 'ccc']
longest(strings) # Output: 'ccc'
```
This function takes a list of strings as input and returns the longest string in the list. It uses the max function to compare all strings in the list and returns the one with the largest length.