```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function is a self-contained solution to the problem you mentioned, using the `contains` method to check if a given substring is present in a string. The function returns a list of all strings from the input list that contain the given substring.