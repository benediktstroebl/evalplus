```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one or None. Returns None if empty input list. """
    
    if not strings:
        return None
    
    if len(strings) == 0:
        return None
    
    return max(strings, key=len)

# Test the function with different input
input_strings = ['a', 'bb', 'ccc', 'xyzz']
result = longest(input_strings)
print(result)  # Output: 'ccc'
``` 
This code defines a function called "longest" that takes a list of strings as input and returns the longest string in the list or None if the list is empty.  It uses the value comparisons and the max function with the key argument set to the length of the string.