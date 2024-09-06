Here's a self-contained Python script that solves the problem of filtering an input list of strings based on a prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix as input parameters. The function uses the
a list comprehension to filter the strings in the list and only include those that start with the specified prefix. 

This problem has been effectively and self-contained in the script, with no external dependencies or functions called.