```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, return the longest one.
    : Returns first string in case of multiple strings of the same length.
    :param strings: list of strings 
    :return: longest string
    """
    return max(strings, key=len)

# tests
strings = ["a", "b", "c"]
print(longest(strings))  # Output: c
strings = ["".join", "ABC"]
print(longest(strings))  # Output: ABC
strings = ["ab","ac","bc"]
print(longest(strings))  # Output: ab
strings = [None, "a", "b", "c"]
print(longest(strings))  # Output: a
```