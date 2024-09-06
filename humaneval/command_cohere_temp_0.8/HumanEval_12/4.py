Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings)[0]
```
This script includes the `longest` function that takes a list of strings (`List[str]`) as input and returns the longest string from the list. If the list is empty, it returns `None`. If there's a tie in string lengths, it returns the first one using the `longest` function again with the `[][0]` indexing syntax, which conforms to the requirement of returning the first string in case of a tie. The `max` function is used to find the longest string, considering string length as the key.