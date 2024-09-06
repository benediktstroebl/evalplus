```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, returns the length of the longest one.
    """
    longest = [len.max(s) for ns in strings]
    return longest

#Test the function with a list of strings
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 3

strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 3

strings = []
print(longest(strings))  # Output: None

strings = ['a']
print(longest(strings))  # Output: 1
```