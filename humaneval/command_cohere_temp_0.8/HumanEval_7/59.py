```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input, and returns a new list containing only the strings from the input list that contain the given substring. This function solves the problem using a list comprehension, filtering out the strings that contain the provided substring. An empty list is returned if the input list is empty or if none of the strings contain the substring.