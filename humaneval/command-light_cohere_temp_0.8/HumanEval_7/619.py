Here is a Python script with a self-contained function that solves the problem of filtering strings that contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This script provides a function `filter_by_substring` that filters an input list of strings and returns a new list that includes only the strings that contain the given substring. The function utilizes the both the list of strings and the substring parameter as its inputs, and returns a new list that contains the strings from the input list that have the substring present in them.

This self-contained function simplifies the problem and provides an elegant solution that can be easily understood and adapted for various use cases.