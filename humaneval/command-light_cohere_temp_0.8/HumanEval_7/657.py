```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -None]
```
This Python script defines a function `filter_by_substring` that filters a list of strings based on whether the substring `substring` is present in each string. It uses the filter method to iterate over the input list and check if each string contains the `substring`. The function returns a new list containing only the strings from the original list that contain the given substring.