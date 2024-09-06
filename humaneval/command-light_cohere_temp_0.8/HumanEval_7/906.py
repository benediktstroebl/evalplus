```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring """
    return [string for string in strings if string.contains(substring)]
```
This script defines a function that filters an input list of strings to only include those that contain a given substring. It uses the` contains()` and `contains()` and checks if the string contains the substring.