```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

The above Python script defines a function called `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain the given substring. 

It uses the typing module for type hints. 

This function solves the problem of filtering strings that contain a given substring by using a simple and efficient algorithm that iterates over the input list and checks if each string contains the given substring.