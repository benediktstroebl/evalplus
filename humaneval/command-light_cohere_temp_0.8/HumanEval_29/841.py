Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. It uses the is list comprehension with the startingswith operator to achieve this.