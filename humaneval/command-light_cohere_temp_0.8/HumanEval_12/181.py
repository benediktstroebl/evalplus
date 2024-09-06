```python
from typing import List
def longest(strings: List[str]):
    """ Outlines a list of strings, returns the length of the longest one.
    return:
        a list of strings
    """
    return max(str.length(string) for string in strings)

# Example usage:
strings = ["a", "bb", "ccc", "abc"]
print(longest(strings))  # Output: 3
```