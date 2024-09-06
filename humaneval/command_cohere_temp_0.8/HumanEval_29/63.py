```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The list comprehension performs the filtering based on the `startswith` method of each string in the list. 

Here's how the function performs on a few test cases:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar')
['array']
```