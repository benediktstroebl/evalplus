Here is a Python script with a self-contained function that solves the problem of filtering strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the contains() method to check if each string in the input list contains the given substring. The function returns a list containing only the strings that contain the substring. 

This is a simple and self-contained way to solve the problem of filtering strings for a given substring.