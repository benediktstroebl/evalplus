Here is a Python script with a self-contained function that filters an input list of strings based on a prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function is designed to filter a list of strings and return a new list containing only the elements that start with the specified prefix. 

It utilizes the `startswith` method to check if each string in the input list starts with the provided prefix.