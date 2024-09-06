```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix`, designed to filter a list of strings and return only those that start with a specific prefix. 

The function utilizes the `startswith` method to check if each string in the list starts with the provided prefix. 

It then converts this test to a list comprehension, creating a new list that contains only the strings that match the condition.