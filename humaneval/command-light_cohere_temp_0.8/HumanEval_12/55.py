Here's the function that solves the problem:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    """
    return max(strings, key=len)
```

Here, the function **longest** takes a list of strings as an argument and returns the longest string in the list, using the **max** function and the **key=len** parameter to sort the strings based on their length. 

This function can be easily incorporated into your markdown code block to solve the given problem and pass corresponding tests.