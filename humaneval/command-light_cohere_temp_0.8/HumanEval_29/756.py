Here is a self-contained Python script that defines a function `filter_by_prefix` solving the problem you described:

```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a') == []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list of strings from the input list that start with the specified prefix. It uses the `startswith` method from Python strings to check if each string in the list starts with the given prefix. 

The function passes all the tests provided.