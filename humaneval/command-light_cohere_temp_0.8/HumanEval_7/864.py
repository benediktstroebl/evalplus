```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. It utilizes the filtering using the the standard Python list comprehension technique. 

This function is self-contained and provides a straightforward and efficient way to solve the problem.