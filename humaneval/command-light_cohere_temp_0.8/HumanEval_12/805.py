Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from the list of strings.
    >>> return longest(['a', 'bb', 'ccc'])
    ['ccc']
    """
    return [x for x in strings if len(x) == max(map(len, strings))]
```
The function `longest` takes a list of strings as input and returns a list of the longest strings from the list. It uses the Python's list comprehension and the `map` function to find the length of each string in the list.