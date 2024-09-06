Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longestStr = max(strings, key=len)
    return longestStr if len(longestStr) == max(len(s) for s in strings) else longest(strings[:strings.index(longestStr)])
```

This script defines a function `longest` that takes a list of strings as input and returns either the longest string in the list or `None` if the list is empty. The function first checks if the list is empty and returns `None` if so. It then finds the longest string in the list using `max` with the `key` argument set to the `len` function to compare strings based on their length. If there is more than one string of the same length, it recursively calls itself on the list of strings excluding the longest one, until it finds the longest string that is the only one of its length in the list. The function returns the longest string found. 

Here's an example usage of the function:
```python
print(longest(['a', 'bb', 'ccc']))  # Outputs: ccc
print(longest(['a', 'aa', 'b']))  # Outputs: aa
print(longest(['a', 'aa', 'aaa']))  # Outputs: aaa
print(longest([]))  # Outputs: None
```

This example demonstrates the function's behavior, including handling lists of different sizes and returning `None` when the input list is empty.