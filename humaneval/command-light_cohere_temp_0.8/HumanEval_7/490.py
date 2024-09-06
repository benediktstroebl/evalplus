```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings for substrings containing the given substring """
    return [s for s in strings if s.find(substring)]
```

This code implements a function **`filter_by_substring`** which filters an input list of strings and returns a new list that contains only the strings that contain the given substring. 
This is achieved using the 'find' method which returns the first index of a match in the string.