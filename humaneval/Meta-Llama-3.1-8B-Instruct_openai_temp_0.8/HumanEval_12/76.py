Here's a simple Python solution for the problem:
```markdown
### Longest String in a List

This script defines a function `longest` that returns the longest string from a given list.
In case of multiple strings of the same length, it returns the first one. If the input list is empty, it returns None.

#### Code
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:  # If the list is empty, return None
        return None
    
    return max(strings, key=len)  # Return the longest string

# Test the function
if __name__ == "__main__":
    print(longest([]))  # None
    print(longest(['a', 'b', 'c']))  # 'a'
    print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

#### Explanation

The function uses the built-in `max` function with the `key` argument set to `len`, which makes it consider the length of each string when determining the maximum value. This approach is more concise and efficient than manually iterating over the list to find the longest string.

Note that the script includes a test at the end to verify that the function behaves as expected.