Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        max_idx = strings.index(max(strings, key=len))
        return strings[max_idx]
```
This script includes the `longest` function that takes a list of strings (`List[str]`) as input and returns the longest string from the list. If the input list is empty, it returns `None`. If there's only one string in the list, it returns the only string. If there are multiple strings of the same length, it returns the first one. The script solves the problem and also handles potential edge cases as per the test cases mentioned in the problem statement. 
The function relies on Python's `index` method to find the first occurrence of the maximum string in terms of length. The `key` argument is used with `len` to sort the strings by length.