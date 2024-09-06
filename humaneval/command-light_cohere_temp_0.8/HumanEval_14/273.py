Here's a self-contained Python function that returns a list of all prefixes from shortest to longest of an input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(itertools.comb.chain_long(prefix)
                    for prefix in string.split('') if prefix)
```
This function uses the `itertools.chain_longest` method from the Python's `itertools` library to generate all possible prefixes from the shortest to the longest.