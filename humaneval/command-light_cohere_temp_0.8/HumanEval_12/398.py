```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    longest_length = max(len(string) for string in strings)
    return strings[strings.index(longest_length)]

# Test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'

strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

strings = []
print(longest(strings))  # Output: None

strings = ['abc', 'abc', 'abc']
print(longest(strings))  # Output: 'abc')
```
The function `longest` takes a list of strings as input and returns the longest string found in the list. It does this by iterating over the list and finding the length of each string in the list using the `max()` function. It then returns the last string found with the maximum length.