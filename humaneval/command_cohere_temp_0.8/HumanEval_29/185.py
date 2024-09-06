```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create lists in Python.

The basic syntax for list comprehension is `[f(x) for x in seq]`, which translates to "Create a new list f(x) for each item x in the sequence seq". The resulting list is composed of the values returned by the function f, which is applied to each item in the sequence.

In the given example, the sequence is the list of strings, and the function f is the filter_by_prefix function, which checks if each string starts with the input prefix (the list comprehension iterates over each element in the list). The result is a new list that contains only the strings that have the desired prefix, regardless of the rest of their content. 

This type of operation in SQL is analogous to using `SELECT` with the `LIKE` operator, where the column would be prefixed with `prefix%`.