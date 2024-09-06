Here is a Python script that contains a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The `filter_by_prefix` function takes in a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. This code is can be used to filter out any string that does not start with the specified prefix.