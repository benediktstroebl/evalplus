Here is a self-contained Python script with a function that filters an input list of strings for those that start with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses the Python list comprehension to filter the strings in the list that have the given prefix. It is using the `startswith` method to check if the given prefix is present at the beginning of a string. It then returns a filter the output as a new list.