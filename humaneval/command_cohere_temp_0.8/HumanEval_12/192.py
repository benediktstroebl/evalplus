Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    longest_string = max(strings, key=len)
    return longest_string
```
This script defines a function called `longest` that takes a list of strings as input and returns either None, or the longest string in the list. If the input list contains only one unique string, the function returns the first occurrence of that string. The `key=len` argument in the `max` function is used to specify that the strings should be sorted by length. This function is designed to accommodate empty input lists, lists with one unique string, and lists with multiple strings of varying or equal lengths, ultimately providing a helpful and concise solution to the problem.