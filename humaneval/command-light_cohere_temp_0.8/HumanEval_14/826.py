Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of the input string:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(itertools.prefix prefixes(string))
```
This function uses the itertools.prefix prefixes function to generate all possible prefixes of the input string.