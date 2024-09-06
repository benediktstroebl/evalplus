```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function utilizes the contains() method to filter a list of strings. It tests for each strings in the input list that contain the provided substring.