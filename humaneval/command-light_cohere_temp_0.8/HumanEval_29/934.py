Here is a Python script that solves the problem of filtering strings based on a prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix as input. The function returns a filtering the result which includes only the strings that start with the given prefix. 

This is a self-contained function, as it can be used to filter a list of strings in a markdown code block without needing external dependencies or functions.