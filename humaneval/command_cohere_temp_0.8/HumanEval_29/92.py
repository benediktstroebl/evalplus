```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. The functionality is illustrated by the following example:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

The `filter_by_prefix` function uses a list comprehension, facilitated by Python's `for` loop, to filter the list of strings (`strings`) based on the given `prefix`. In detail, it iterates over each string in the list and checks whether it starts with the specified prefix. Strings that meet this condition are included in the return list, while those that do not are excluded.