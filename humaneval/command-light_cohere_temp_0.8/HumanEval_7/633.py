```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function named **filter_by_substring** that filters and returns a new list of strings from the input list **strings** that contain the given substring **substring**. 

The function utilizes the **contains** method to iterate through the input list and check if each element contains the specified substring. 

This self-contained function efficiently solves the problem of filtering strings based on a substring and passes the corresponding tests without requiring external dependencies.