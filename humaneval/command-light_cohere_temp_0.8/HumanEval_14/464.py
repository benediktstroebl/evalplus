```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    A prefix is a string that can be derived from the input by removing characters
    from the left (starting from the leftmost character) until finding a null.
    character.

    The strings that strings are built up by concatenating other strings. The 
    order is determined by the length of the prefix string.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [c for c in string if c != '']
```