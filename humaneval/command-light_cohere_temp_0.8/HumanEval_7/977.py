```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. It uses the select function on each string in the input list and passes the test by checking if the resulting list contains the substring too.

This function follows Python's type hints for better readability and can be used with most Python dialects.