```python
from typing import List
def longest(strings: List[str]):
    """ Out of list of strings, return the longest one
    """
    return max(strings, key=len)

# Example usage:
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
```

In this code, the `longest()` function takes a list of strings as an argument. It uses the `max()` function with the `len` key as the `key` argument to find the string with the maximum length in the input list.

Note that this code provides a fully self-contained solution to the problem and can be used as a standalone Python script.