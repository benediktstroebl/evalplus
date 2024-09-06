Here is a Python script that has a self-contained function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list comprehension to filter out the strings from the input list that start with the given prefix. It does not rely on any external imports or functions – It is a self-contained and efficient way to solve the given problem.