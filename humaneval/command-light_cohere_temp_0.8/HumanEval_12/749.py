```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    >>> longest(['a', 'b', 'c']) == 'a'
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with valid inputs and checks
# Test with an empty list
print(longest([]))

# Test with one string
print(longest(['a']))

# Test with one string of each different length
print(longest(['a', 'bb', 'ccc']))
```
The function `longest` accepts a list of strings as input and returns the longest string in the list. It returns `None` if the input list is empty. The function uses the max function with the `key` parameter set to the length of each string in the list, which returns the largest one. The function also handles the case of one string of different lengths and another case of an empty list.