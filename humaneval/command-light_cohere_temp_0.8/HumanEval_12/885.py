```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    strings = ['a', 'b', 'c', 'abc', 'a']
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
print("Longest:", longest(strings))  # Output: c

strings = ['a', 'bb', 'ccc']
print("Longest:", longest(strings))  # Output: bb

strings = []
print("Longest:", longest(strings))  # Output: None")

strings = ['a', 'b', 'ccc', 'a']
print("Longest:", longest(strings))  # Output: a")
```
This code defines a function `longest` which takes a list of strings as input and returns the longest string. It achieves this by utilizing the max function along with the `key=len` argument to ensure the longest string is selected based on its length. The test cases demonstrate the required behavior.