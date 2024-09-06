```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    if not strings:
        return None
    lst = [str.length(s) for s in strings]
    return max(lst)
# Example usage:
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 3
``` 
This script defines a function called `longest` that takes a list of strings as input and returns the length of the longest string in that list. It utilizes the maximum function to get the maximum length.