Here is a self-contained Python script with a function that solves the problem of returning the longest string among an input list of strings:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    """
    if not strings:
        return None
    
    max_len = max([len(s) for s in strings])
    longest_str = strings[0]
    for s in strings:
        if len(s) == max_len:
            longest_str = s
    
    return longest_str

# Example usage
strings = ['a', 'b', 'c', 'd']
longest_result = longest(strings)
print(longest_result)
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. It also includes sample usage of the function to pass tests.