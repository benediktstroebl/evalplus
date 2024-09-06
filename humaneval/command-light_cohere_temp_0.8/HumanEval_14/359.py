```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ['a', 'ab', string.make_list(string)][0]
```
This function iterates through all possible prefixes and returns the list of all prefixes from shortest to longest.