Here is a self-contained Python script that includes the function `filter_by_prefix` which solves the problem of filtering an input list of strings based on a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix as input parameters. It uses the string matching to filter the list of strings, keeping only those that start with the given prefix. The function returns a list of matching strings.