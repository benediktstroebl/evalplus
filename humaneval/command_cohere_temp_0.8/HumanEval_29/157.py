```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This is achieved using a list comprehension, filtering out the elements that have a prefix that matches the specified prefix.

The behavior is illustrated in the following example:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'arr')
['array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'unknown')
[]
``` 

It successfully filters the list of strings based on the provided prefix, optimizing the list to include only the relevant strings.