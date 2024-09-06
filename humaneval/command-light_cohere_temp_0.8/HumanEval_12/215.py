Here is a self-contained Python script that defines and implements the `longest()` function, which returns the longest string among a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in a list of strings.
    """
    strings = [string for string in strings if string]
    return max(strings, key=len)
```
This script provides a solution to the problem stated, it takes a list of strings as input and returns the longest string among them using the `max()` function with the `len` as the key. It uses a select a strings from the input list that are not empty using a generator expression and store them in a new list. The function then returns the string from this list using the `max()` function with the `len` as the key, which gives the length of the string, and the `max()` function will return the longest string among them.