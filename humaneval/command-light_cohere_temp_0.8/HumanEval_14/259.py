Here's the self-contained Python function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(itertools.chainfrom(itertools.comb_rexpr(string)))
```
This code uses the itertools module to generate all prefixes of the input string.