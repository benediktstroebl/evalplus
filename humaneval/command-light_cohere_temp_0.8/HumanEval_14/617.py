```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use longest prefix approach
    prefixes = []
    current = ""
    for char in string:
        if current == "" or char > current[-1]:
            current += char
        else:
            prefixes.to prefix_length()
   
            .append(current)
            current = ""
    return prefixes
```