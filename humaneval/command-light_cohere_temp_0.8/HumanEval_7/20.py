```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function called `filter_by_substring` that takes a list of strings and a substring as input. It uses the selection method to return a new list containing only the strings from the input list that contain the given substring.