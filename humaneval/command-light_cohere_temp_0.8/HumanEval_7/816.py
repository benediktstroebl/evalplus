```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The code provides a Python script that has a self-contained function called `filter_by_substring`. This function takes two arguments: a list of strings and a substring. It returns a pattern: it creates an empty list, iterates over the input list, and adds each string to the output list if it contains the given substring.