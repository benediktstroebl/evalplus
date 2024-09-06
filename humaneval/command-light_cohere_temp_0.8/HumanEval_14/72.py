```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use the slicing notation to get all prefixes
    prefixes = [char for char in string if char != '']
    return prefixes
```