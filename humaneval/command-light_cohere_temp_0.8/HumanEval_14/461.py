Here's the self-contained Python script that defines a function to return a list of all prefixes from shortest to longest of the input string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']

    """
    if not string:
        return []

    # Use a trie to generate all prefixes
    prefixes = set()
    t = str.join(string)
    if t == "" and string[0] != " ":
        t = string[0]

    for c in t:
        if c != " ":
            prefixes.add(str.join(c))

    return prefixes
```