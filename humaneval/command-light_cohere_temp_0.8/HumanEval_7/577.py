```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python script defines a function named `filter_by_substring` that takes a list of strings and a substring as input. The function uses a list comprehension with the `find` method to check if each string in the input contains the given substring. This function returns a full list of strings that contain the specified substring.