```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It returns a using the method list comprehension, filtering the input list to only include strings that start with the given prefix. This function is a straightforward way to solve the problem and is self-contained within the script, as it does not require any additional imports or global variables.