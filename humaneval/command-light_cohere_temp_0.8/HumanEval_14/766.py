```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use a dictionary to hold the prefix mapping
    prefix_map = {
        'a': [], 'ab': ['b'], 'abc': []
    }

    # Build the initial prefix map
    for char in string:
        if char in prefix_map:
            prefix_map[char].append(char)
        else:
            prefix_map[char] = [char]

    # Return the list of all prefixes
    return prefix_map. 
```  This can be used to find all prefixes of any given string.