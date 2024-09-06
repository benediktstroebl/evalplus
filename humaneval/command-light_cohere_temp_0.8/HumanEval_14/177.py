Here is a Python script that contains a self-contained function that returns all prefixes from shortest to longest of any input string:
```python
from typing import List
import string

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []
    # define length of each prefix
    lengths = [1] + map(len, string)
    # sort the list of lengths ascendingly
    lengths.sort()
    wide_to_smallest()
    # loop through the sorted list of lengths and pick a starting index
    i = 0
    while i < len(lengths):
        if lengths[i] == lengths[i-1]:
            i += 1
        else:
            break
        j = i
        while j < len(string):
            yield string[j:j+lengths[i]]
            j += lengths[i]
    return []
``` 
This function utilizes the map and sort functions to efficiently generate all prefixes from the shortest to the longest of the input string.