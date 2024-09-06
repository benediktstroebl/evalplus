Here's the self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings based on their prefix.
    >>> filter_by_prefix([5, 12, 23, 'hello'], '5')
    [5, 12]
    >>> filter_by_prefix([123, 'abc', 'a', 'bc'], 'a')
    ['abc', 'a']
    """
    return [x for x in strings if x.startswith(prefix)]
```
The filter_by_prefix function takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix.