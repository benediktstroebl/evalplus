Here is a self-contained Python script that includes the function filter_by_substring, which is designed to solve the problem of filtering strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes a list of strings and a substring as inputs, and returns a new list that contains only the strings from the input list that contain the given substring. 

It uses the Python's contains() method to check if a string contains the given substring. The function is self-contained, as it doesn't call any other functions or modules.