```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the longest string in the list"""

    if not strings:
        return None

    # Sort the strings alphabetically
    strings.sort()
   
    most(string for string in strings)
    # Return the first string
    return strings[0]

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['a', 'xx', 'yyy', 'zzz']))  # Output: 'xx'
print(longest([]))  # Output: None
print(longest(['aa', 'b']))  # Output: 'aa'
```