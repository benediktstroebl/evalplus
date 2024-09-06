Here is a self-contained Python script that solves the problem of filtering an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function called **filter_by_substring** that takes a list of strings and a substring as input and returns a new list that contains only the strings from the input list that contain the given substring. The function uses the previous method to search for the substring.

This function is self-contained, and it does not rely on any external libraries or modules. It can be easily to test and understand how it works without relying on external code.