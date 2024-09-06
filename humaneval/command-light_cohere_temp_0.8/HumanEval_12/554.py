```python
from typing import List
def longest(strings: List[str]):
    """
    Return the longest string from the list of strings.
    """
    return max(strings, key=len)

# Test case
test_strings = ['a', 'b', 'c', 'xx']
longest(test_strings) # Output: c
```
This function takes a list of strings as input and returns the longest string in that list, using the `max()` function and the `key=len` parameter to order the strings by length. 
In this case, the function will return 'c' as it is the longest string in the list.