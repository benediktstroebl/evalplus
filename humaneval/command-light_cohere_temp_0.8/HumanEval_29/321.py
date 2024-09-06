Here is a Python script with a self-contained function that solves the problem you described:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that takes in a list of strings and a prefix, and returns a new list that contains only the strings that start with that prefix. The function utilizes the method `startswith` to check if each string in the input list starts with the given prefix.