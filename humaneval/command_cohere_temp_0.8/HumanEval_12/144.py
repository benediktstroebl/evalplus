Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    longest_str = max(strings, key=len)
    return longest_str
```
This script defines a function `longest` that takes a list of strings as input and returns either None if the input list is empty, or the longest string in the list while retaining the first occurrence in case of equal lengths. The logic employed employs a simple max computation using the `len` function as the key. An additional check for single unique length ensures that the function returns the only string in the list if it is of the longest length. 

Here is some insight into how the function can be validated:
```python
# Test Scenarios
assert longest([]) is None
assert longest(['a', 'b', 'c']) == 'a'
assert longest(['a', 'bb', 'ccc']) == 'ccc'
assert longest(['a', 'aa', 'aaa']) == 'aaa'
``` 

This way, you can confidently assert the function's behavior against various test scenarios.