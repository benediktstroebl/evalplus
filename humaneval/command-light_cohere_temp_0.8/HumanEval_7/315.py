```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python script defines a function called `filter_by_substring` that takes in two parameters: a list of strings and a substring. The function then returns a list of strings from the input list that contain the given substring.