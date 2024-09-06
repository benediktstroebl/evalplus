Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)  # Get the longest string
    if len(set(strings)) == 1:  # If there is only one string of that length
        return longest_string
    return longest.func_first_occurrence(longest_string, strings)

def func_first_occurrence(longest_string, strings):
    return next((s for s in strings if s == longest_string), strings[0])
```

This script defines a function `longest` that takes a list of strings as input and returns either the longest string in the list, the first string of the same length in case of multiple longest strings, or `None` if the input list is empty. It employs the `max` function to determine the longest string and leverages `next` and a generator expression to identify the first occurrence of the longest string.

This solution has a reusable helper function `func_first_occurrence` that identifies the first occurrence of a given string within a list of strings.