```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This Python code implements a function `filter_by_substring` that filters an input list of strings to include only those that contain a given substring. It uses the Python's list comprehension with the `find()` method to check if each string contains the given substring. 

The `find()` method returns the position of the first occurrence of the substring, so the function filters the input list by keeping only the strings that have that substring.