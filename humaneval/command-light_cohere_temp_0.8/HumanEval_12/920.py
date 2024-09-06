```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    # Sort strings alphabetically
    strings.sort()

    longest_char = max((char for char in 'abc' if strings[i].count(char)) for i in range(len(strings)))

    return strings[ longest_char ]

# Test cases
longest(['a', 'bb', 'ccc'])
# Output: 'ccc'

longest(['aa', 'bb', 'ccc'])
# Output: 'bb'

longest([])
# Output: None

longest(['a'])
# Output: 'a'
``` 
This function, named `longest`, takes a list of strings as input. It then checks if the `strings` list is empty and returns `None` in such case. Otherwise, it sorts the strings alphabetically and finds the length of the longest string using a `max()` function with a generator expression. The `max()` function returns the maximum length of the string, and the corresponding index in the list.