```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This behavior is demonstrated in the example below:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
``` 

The code demonstrates how the `filter_by_prefix` function effectively filters the input list to include only those strings that begin with the given prefix `'a'` respectively.