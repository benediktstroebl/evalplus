Here is a self-contained Python script that includes a function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix, and returns a new list that contains only the strings from the input list that start with the specified prefix. The function is designed to pass all the tests that are relevant for this problem.