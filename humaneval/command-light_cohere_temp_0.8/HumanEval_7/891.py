Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

The code you have provided has a function named `filter_by_substring` that takes a list of strings and a substring as input. It uses the `find()` method to find the substring in each string and returns the list of strings that contain the given substring.