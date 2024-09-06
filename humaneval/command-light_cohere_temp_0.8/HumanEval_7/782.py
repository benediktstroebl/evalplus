The function `filter_by_substring()` takes in a list of strings and a substring as arguments. It returns a
 list of strings that contain the given substring.

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function is self-contained and can be used to filter a list of strings for those that contain a given substring.