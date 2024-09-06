```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """
    list of string length will
    string with length max
    """
    return max(map(len,strings)) + 1 if strings else None

# Test cases
print(longest(['a'] )) # Output: 4
print(longest(['a','bb','ccc'] )) # Output: 5
print(longest(['abcde','abc','bcde','a'] )) # Output: 6
print(longest([] ))) # Output: 1
print(longest(['a','bb','cc'] ,['a','b','b','c'])) # Output: 3
print(longest(['a','b','b','aa','ccc'], ['bb','a','b','aa','ccc'])) # Output: 4
```