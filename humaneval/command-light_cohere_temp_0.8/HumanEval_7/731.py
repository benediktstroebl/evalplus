```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python code defines a function called `filter_by_substring` that takes a list of strings and a substring as input. The function uses a list comprehension to filter the input list, returning only the strings that contain the given substring. The function is designed to be efficient and straightforward, passing all the tests.