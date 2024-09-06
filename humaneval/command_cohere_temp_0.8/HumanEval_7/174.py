```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings (`strings`) and a substring (`substring`) as input and returns a new list of strings that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including those that contain the substring `substring`. This solution adheres to the specified problem and provides an efficient way to filter strings based on a substring.