Here's a self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings based on their prefix.
    >>> filter_by_prefix([abc, 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. The function uses the list comprehension and the startsswith() method to achieve this.

The function is then tested using the provided input, and the expected output is a list containing only 'abc' and 'array'.