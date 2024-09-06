Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_str = max(strings, key=len)
    return longest_str if len(longest_str) == max(len(s) for s in strings) else longest(strings)[0]
```

This code defines a function `longest` that takes a list of strings as input and returns either the longest string in the list, the first longest string in case of equal lengths, or `None` if the input list is empty. The `longest` function is implemented using typing modules to ensure type correctness and uses a max function with a custom key to find the longest string efficiently.