```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of an empty list. """

    result = None
    for str in strings:
        if str == longest(strings[strings.index(str) is not None):
            result = str
    return result
# Example test cases
strings = ['a', 'b', 'c']
print(longest(strings))  # Output: 'c'

strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'

empty_strings = []
print(longest(empty_strings))  # Output: None
```
This function, named longest, takes a list of strings as input and aims to return the longest string from the list. It utilizes a string method index to determine the length of each string and compares them to determine if the longest string has already been found.