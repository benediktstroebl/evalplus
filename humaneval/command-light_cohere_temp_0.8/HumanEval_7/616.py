Here is a Python script that contains a self-contained function that solves the problem of filtering strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list of strings that contain the substring. 

We use the method `find()` to search if the substring exists in the given string or not.