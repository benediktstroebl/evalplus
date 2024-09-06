Here's the self-contained Python function to generate all prefixes from the shortest to the longest:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(itertools.chain(string))
```
Do you require any further assistance with this?