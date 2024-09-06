Here's the self-contained Python script that solves the problem of concatenating strings:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)
```
This code defines a `concatenate` function that takes a list of strings as input and returns the concatenated string. It uses the particular `join list comprehension` to create a new string by joining the elements of the input list. This function is run-time test by passing an empty list (`[]`) and a list with only one string ('a') to ensure the expected output is an empty string.