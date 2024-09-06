Here is a self-contained Python function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(itertools.prefixic_tails(string))
```

The function itertools.profileUNT as prefixes from the short enough substring of the input string, and then concatenates them to get the full list of prefixes.