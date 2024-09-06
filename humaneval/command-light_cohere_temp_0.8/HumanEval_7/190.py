```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function takes a list of strings and a substring as input, and it returns a new list that contains only the strings from the input list that contain the given substring. 

The function uses the Python's list comprehension with the 'contains' method to check if each string in the input list contains the given substring.