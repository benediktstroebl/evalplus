```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This function uses the find() method to check if each string in the input list contains the given substring.  The function is designed to work with lists of strings, and it returns a new list that contains only the strings that contain the given substring.