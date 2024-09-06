Here is a Python script with a self-contained function that solves the problem of filtering strings for a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
```

This function takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. The function uses the same built-in substring. Notice that this method is self-contained and does not require external functions or built-ins.