```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. 

The function uses the Python's built-in `contains` method, which checks if a given substring is present within a string. 

This is a self-contained solution, as it does not rely on any other functions or modules in its definition.