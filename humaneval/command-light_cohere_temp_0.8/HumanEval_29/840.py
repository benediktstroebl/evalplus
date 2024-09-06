Here is a self-contained Python script that implements the provided function `filter_by_prefix` and passes all the tests:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a') == []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]
```

The `filter_by_prefix` function takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. The function uses the process that uses the `startswith` method of the strings in the list to filter the strings.

It's a self-contained solution and passes the tests provided.