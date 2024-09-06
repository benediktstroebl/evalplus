```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring` as input. It returns a new list containing only the strings from `strings` that contain the specified substring. To achieve this, it uses a list comprehension, iterating over each string in `strings`, and including only those that have the `substring` present in them.