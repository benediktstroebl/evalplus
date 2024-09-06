```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that filters an input list of strings and returns a new list that contains only the strings that start with a specified prefix. It utilizes the tested type hint **List[str]** to ensure the function works with strings as expected.