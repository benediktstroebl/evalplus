Here's the solution:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Return the length of the longest string in the list
    """
    max_len = min_len = len(strings[0])
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
        if len(string) == max_len:
            min_len = len(string)
    return min_len
```
This code provides a solution to the problem you provided. It calculates the longest string length by comparing the lengths of all input strings. The code uses the different variables: `max_len` and `min_len` to track the maximum and minimum string lengths.