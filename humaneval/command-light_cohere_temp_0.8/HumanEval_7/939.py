Here is a self-contained Python script that solves the problem of filtering strings that contain a given substring: 
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function, `filter_by_substring`, which takes a list of strings and a substring as input and returns a new list that contains only the strings that contain the given substring. 

The `contains` method tests if each string in the input list contains the given substring using the `contains` method.