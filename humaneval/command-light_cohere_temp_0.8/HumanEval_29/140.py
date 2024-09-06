Here's a self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix parameter. It returns a filtered list of strings that start with the given prefix. It utilizes the Python's list comprehension to filter the strings.

The function is self-contained, and it passes the tests provided in the problem statement. 

Please note that you can use this function to solve the problem by simply passing your test data as parameters.