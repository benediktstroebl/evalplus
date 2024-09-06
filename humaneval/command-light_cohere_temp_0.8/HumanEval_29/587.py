```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. The function uses the filtering to return a new list that contains only the strings from the input list that start with the given prefix. The function utilizes the test cases to verify its behavior, demonstrating a self-contained solution for filtering strings based on a given prefix.