```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension, which is a powerful Python construct to create new lists by applying a condition to each element of the existing list. 

To use the `list comprehension`, the function iterates over each element `strng` in the `strings` list and applies the condition `strng.startswith(prefix)`, which checks if the current string starts with the provided prefix. 

This condition is satisfied if the current string is equal to the prefix string, or if the current string is longer than the prefix string and the prefix is a prefix of the current string. In other words, the condition checks if the `prefix` counts as a `prefix` of any string in the `strings` list. 

The `return_list` is constructed by including only those strings from `strings` that satisfy the condition. 

The function's behavior is illustrated in the docstring in the following way:
```python
"""
Filter an input list of strings only for ones that start with a given prefix.

Examples:
>>> filter_by_prefix([], 'a')
[]

>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
"""
```

The first example with empty input illustrates that an empty list should be returned when an empty list is provided as input. The second example shows the correct behavior of the function when some strings start with the prefix and others do not. The resulting list, `[ 'abc', 'array' ]`, is appended at the end of the docstring as a comment to provide a more detailed understanding of the function's behavior on a specific input.