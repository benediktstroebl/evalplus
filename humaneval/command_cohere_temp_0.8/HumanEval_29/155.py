```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is achieved using a list comprehension, filtering out the elements that have a prefix that doesn't match the specified prefix.

Here is an example of how to use this function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'arr')
['array']
```

The function helps filter strings that have a specific prefix without modifying the original list, thus providing a streamlined way to perform such filtering and querying operations.