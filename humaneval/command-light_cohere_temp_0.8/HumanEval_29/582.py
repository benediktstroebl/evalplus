```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    : Returns a Filtering logic goes like:  Compare the first character of every string to the prefix.
    Returns: list of all strings starting with the given prefix.
    """
    Filtering code example:
    prefix == string[0] for every string in the input list
    """
    return [string for string in strings if prefix == string[0]]
```