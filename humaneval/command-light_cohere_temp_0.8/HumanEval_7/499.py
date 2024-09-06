```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It returns a  a list of strings from the input list that contain the given substring. 

The function uses the `contains` method to iterate through the list of strings and returns only those that contain the given substring.