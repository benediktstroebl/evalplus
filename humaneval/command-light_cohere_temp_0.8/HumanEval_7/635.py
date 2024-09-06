Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for ones that contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This function utilizes the contains() method to check if each string in the input list contains the given substring. It then returns a