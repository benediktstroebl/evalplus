Here's the self-contained Python function that solves the problem of finding all prefixes from shortest to longest of a given input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return list(nx for x in string if x != ' ')
```  This function uses a generator expression to iterate over every character in the input string, and excludes spaces to generate the prefixes.