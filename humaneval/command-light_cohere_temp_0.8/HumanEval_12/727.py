```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string from a list of strings.
    Args:
    strings: list of strings
    Returns:
    the longest string in strings, or None if empty.
    """
    return max(strings, key=len)

# Tests
strings = ['a', 'b', 'c']
longest(strings)  # Output: 'c'
strings = []
longest(strings)  # Output: None
strings = ['aa', 'bb', 'ccc']
longest(strings)  # Output: 'ccc'
``` 
The function 'longest' in the code above takes a list of strings as input and returns the longest string in the list. The function utilizes the max function with a key=len argument, which gives the length of each string in the list. The function then returns the max with the longest length, which is also None if the list is empty.