```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This code defines a function **filter_by_substring** that takes a list of strings and a substring as input and returns a new list that contains only the strings from the input list that contain the given substring. 

The function uses the Python list comprehension to iterate through the input list of strings and checks if each string contains the given substring. 

The function is self-contained, and it can solve the problem of filtering strings that contain a given substring.