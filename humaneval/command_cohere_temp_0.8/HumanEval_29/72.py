```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This behavior is demonstrated in the following example:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

The `filter_by_prefix` function utilizes a list comprehension, creating a new list by filtering strings that start with the provided prefix. This efficient approach simplifies the creation of new lists, avoiding the need to manually iterate over the input list and reducing the complexity from O(n) to O(nLICENSE).