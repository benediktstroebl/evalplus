```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The syntax `s for s in strings if s.startswith(prefix)` creates a list of all elements in `strings` that have a prefix that matches the `prefix` parameter. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example uses the input list `['abc', 'bcd', 'cde', 'array']` and the prefix, `a`. The function returns only the two strings that start with the specified prefix, 'a': 'abc' and 'array'. 

The function guarantees that any string it returns necessarily has the specified prefix, as long as the prefix is a non-empty string and not longer than the length of any string in the input list.