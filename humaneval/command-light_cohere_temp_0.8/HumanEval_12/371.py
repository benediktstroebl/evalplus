Here's the solution:
```python
from typing import List

def longest(strings: List[str]) -> str:
    # check if list is empty
    if not strings:
        return None
    # Initialize max length
    max_length = 0
    # compare and update max length
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
    return max_length
```