```python
from typing import List
def longest(strings: List[str]):
    """ Returns the length of the longest string in the list.
    """
    max_len = 0
    longest_str = ""
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            longest_str = string
    return longest_str
# Uncomment the function and pass the test
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: ccc
```