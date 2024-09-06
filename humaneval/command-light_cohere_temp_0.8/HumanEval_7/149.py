Here is a Python script that contains a self-contained function `filter_by_substring` that filters a list of strings based on whether the strings contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function uses the `contains` method to check if each string in the input list contains the given substring. It returns a filter the also a list of strings that contain the substring, as a result.