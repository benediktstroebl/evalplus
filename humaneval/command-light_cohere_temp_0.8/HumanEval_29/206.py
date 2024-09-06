Here is a Python script with a self-contained function that solves the problem of filtering strings by prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list comprehension to filter a list of strings and only returns the strings that start with the given prefix. It passes all tests by prefix 'a' and a list of strings ['abc', 'bcd', 'cde', 'array'] and the prefix 'a' successfully.