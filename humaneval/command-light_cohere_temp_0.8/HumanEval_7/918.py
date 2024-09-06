```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python script defines a function called `filter_by_substring` that filters and returns a new list containing only those strings from the input list that contain the given substring.  The function utilizes the Python's `contains` method to check if each string in the input list contains the given substring.