```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    >>> longest([]) --> Returns None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['a', 'aa', 'aaa'])
    'aaa'
    """
    return max(strings, key=len)

# Run the function and test the results
print(longest(['a', 'b', 'c']))  # Output: 'a'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['a', 'a', 'aa', 'aaa']))  # Output: 'aaa'
```
The function `longest` takes a list of strings as input and returns the longest string in the list. 
The function uses the `max` function with the `key` argument set to `len` to find the maximum value of the length of the string.