Here is a Python script that contains a self-contained function that filters an input list of strings for those that start with a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses the Python list comprehension and the starts with operator to filter out the strings that start with the given prefix. 

The function then returns a new list containing only the filtered strings.