```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. This is achieved using a list comprehension, filtering out the elements that have a prefix that doesn't match the input `prefix` string.

The behavior is illustrated in the docstring example:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
``` 

The first example, with an empty list and the prefix 'a', returns an empty list. The second example, with the list ['abc', 'bcd', 'cde', 'array'] and the prefix 'a', returns a list with ['abc', 'array']. As expected, the list filtration matches the strings with the given prefix regardless of the following characters.