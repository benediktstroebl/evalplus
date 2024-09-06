```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. The syntax `s for s in strings if s.startswith(prefix)` creates a list of all elements in `strings` that have a prefix that matches the `prefix` parameter. 

Here is an example usage of the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example returns only the strings that start with the character 'a'.