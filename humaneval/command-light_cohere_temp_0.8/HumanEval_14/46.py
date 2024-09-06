```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []
    
    # Use Python's built-in methods to get prefixes
    return [prefix for prefix in string.split('') if prefix]
```