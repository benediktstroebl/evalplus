```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code defines a function `filter_by_substring` that takes in a list of strings and a substring as input. It uses theis straightforward list comprehension to filter the input list based on whether each string contains the given substring.