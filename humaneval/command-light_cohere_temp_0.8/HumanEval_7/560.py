```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]
```

This function accepts a list of strings and a substring as arguments. It returns a filter the the list of strings that contain the substring. The function utilizes the `find()` function to locate the substring within each string and then uses the `[] if not found` condition to filter out the strings that do not contain the substring. 

This function is self-contained, and it can be used to filter a list of strings for a given substring.