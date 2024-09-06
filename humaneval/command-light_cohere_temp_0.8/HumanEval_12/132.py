```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one or None if empty"""
    if not strings:
        return None
    return max(strings, key=len)
# Example usage:
strings = ['a', 'b', 'c', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = []
print(longest(strings))  # Output: None
``` 
This solution passes all the tests specified in the prompt. In the code, we first define a function that takes a list of strings as input. The code then checks if the list is empty, then it returns None. If the list is not empty, it returns the string with the maximum length in the list, using the `max()` function with the `key=len` argument, which ensures that the longest string in the list is selected.