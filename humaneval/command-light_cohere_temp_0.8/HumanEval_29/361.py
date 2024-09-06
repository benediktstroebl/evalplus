```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code implements a function called `filter_by_prefix` that filters a list of strings based on a given prefix. 

The function takes two parameters: a list of strings `strings` and a prefix `prefix`. It returns a new list that contains only the strings from the input list that start with the specified prefix.

For example, if you call this function with the list of strings ['abc', 'bcd', 'cde', 'array'], and the prefix 'a', it will return the list ['abc', 'array'].