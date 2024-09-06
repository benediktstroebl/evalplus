Here is a self-contained Python script that includes a function `longest` which determines and returns the longest string from a list of strings:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one
    """
    if not strings:
        return None
    
    max_length = max(len(string) for string in strings)
    
    return strings[max_length - 1]

# Test the function with various inputs
longest(['a', 'b', 'c'])  # Output: 'a'
longest(['a', 'bb', 'ccc'])  # Output: 'ccc'
longest([])  # Output: None
longest(['a', 'bc', 'abc'])  # Output: 'abc'
```
The function `longest` takes a list of strings as input and returns the longest string from that list. This is the maximum length of each string in the list is calculated using the `max` function. The `[max_length - 1]` is used to return the actual character of the longest string.