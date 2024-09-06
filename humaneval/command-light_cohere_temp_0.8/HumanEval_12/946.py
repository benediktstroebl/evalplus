```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    >>> return None if strings is empty
    >>> longest([])
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test case:
strings = ["a", "b", "c", "aa", "bb", "ccc"]
print(longest(strings))  # Output: ccc

# Test case:
strings = []
print(longest(strings))  # Output: None
```
This Python code defines a function called "longest" that takes a list of strings as input and returns the longest string in that list. It uses a "typing" to provide type hints and ensure the function works with any list of strings, regardless of their length or content. 

The code also has two test cases: first, an empty list, and second, a list of different characters. These test cases are passing the good.