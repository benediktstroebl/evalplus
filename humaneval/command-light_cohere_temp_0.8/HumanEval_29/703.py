```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python function takes a list of strings and a prefix as input and returns a new list that includes only the strings from the input list that start with the given prefix. It uses the basic list comprehension to filter the strings. The function is self-contained and passes the tests with the provided input.