```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension, which is a concise way of expressing a for loop in Python.

The basic syntax for list comprehension in Python is `[f(x) for x in seq]`, which maps the function or transformation f across the elements of sequence seq to produce a new list. The `if` statement in the list comprehension is used for filtering out only the strings that start with the prefix in the given list of strings.