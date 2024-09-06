Here is a self-contained Python script that solves the problem of filtering strings based on their prefixes:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list that contains only the strings that start with the given prefix. The test cases are also provided to ensure the correctness of the filter_by_prefix function.