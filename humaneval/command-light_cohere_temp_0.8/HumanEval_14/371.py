```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [''.join(string[i:]) for i in range(len(string)) if string[i:].isalpha()]
```