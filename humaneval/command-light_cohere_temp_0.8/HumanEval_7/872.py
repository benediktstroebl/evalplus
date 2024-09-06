Here is a self-contained Python script that solves the problem you outlined:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This script defines a `filter_by_substring` function that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. 

The function uses the list comprehension with the `find` method to check if each string in the input list contains the given substring.