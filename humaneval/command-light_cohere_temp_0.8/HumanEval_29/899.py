Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. It uses the basic list comprehension to filter the strings. The function is self-contained, as it does not call any other functions or modules and only uses built-in Python functions and types.