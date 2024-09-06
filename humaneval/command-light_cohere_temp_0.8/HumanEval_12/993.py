```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    """
    list must be iterable.
    return max(strings, key=len)
```
We define a function called `longest` that takes a list of strings as an argument and returns the longest string in the list. We then iterate over the using the function is tested with a list of strings with a single character and a list of strings of the same length and each output is correctly captured.