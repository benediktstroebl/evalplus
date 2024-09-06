```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`, as input and returns a new list, `return_list`, of strings from `strings` that start with the given `prefix`. It uses a list comprehension to iterate through each string in `strings` and returns the ones that start with the `prefix`. If the `strings` list is empty or `prefix` is empty, the function returns an empty list.

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This would return a list of strings that start with the prefix "a", resulting in a return value of `['abc', 'array']`. 

This approach utilizes Python's string `startswith` method and the list comprehension to efficiently filter the strings according to the problem statement.