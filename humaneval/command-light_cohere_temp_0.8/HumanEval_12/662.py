```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.
    >>> return longest(['a', 'bb', 'ccc'])
    """
    # Use the max function to find the length of the longest string
    return max(strings, key=len)

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['a', 'aa', 'ccc'])))  # Output: 'aa'
print(longest([])))  # Output: None
print(longest(['aa', 'a', 'a']))  # Output: 'aa'
```

The function `longest` takes a list of strings as input and returns the longest string. It uses the max function with the `key=len` parameter to find the length of the longest string. It then returns the max of the list with the `key` parameter set to the length of the string.

The function is then tested with different inputs and the results are printed to the console.