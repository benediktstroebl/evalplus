```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python function utilizes the contains() method to check if each string from the input list contains the given substring. The function then returns a list of all the strings from the list that contain the substring.

This is a self-contained solution to the problem of filtering strings for a given substring, and it passes all the corresponding tests.