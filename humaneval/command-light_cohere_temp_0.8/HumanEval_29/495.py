Here's a self-contained Python script that defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a solution for the problem you described. It efficiently filters the through a list of strings and returns a new list containing only the strings that have the specified prefix. 

This solution is self-contained, meaning it doesn't rely on any external imports or functions, and can be fully expressed within the code block.