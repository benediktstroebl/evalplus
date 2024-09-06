```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring`. It returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, where each string in the input list is checked for the presence of the substring, and those that contain it are included in the resulting list.