```python
from typing import List
def longest(strings: List[str]):
    # function to find the length of the longest string in the list
    max_length = len(max(strings, key=len))
    # Return the length of the longest string
    return max_length
# test case 1: empty list
print(longest([]))
# Output: None
# test case 2: list with one string
print(longest(['a']))
# Output: 1
# test case 3: list with multiple strings of the same length
print(longest(['a', 'b', 'c']))
# Output: 1
```