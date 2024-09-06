Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    longest_string = max(strings, key=len)
    return longest_string
```

This script defines a function called `longest` that takes in a list of strings as input and returns either `None` or the longest string among the inputs, considering ties to return the first occurring string in the list. The function first checks if the list is empty and returns `None` if so. It then checks if there is only one string in the list and returns that string. If there is more than one string, it uses the `max` function with a custom key function to compare strings based on their length to find the longest one.