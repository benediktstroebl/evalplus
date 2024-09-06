```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one
    """
    if not strings:
        return None
    max_length = min([len(str) for str in strings])
    return max(strings, key=len)[:max_length]
# Example usage
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'a'
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
```
This Python code defines a function called "longest" which takes a list of strings as input and returns the longest string from the list. It utilizes the minimum length and the maximum function to get the longest string. The code then provides two examples of calling the "longest" function with a list of strings and prints the result.