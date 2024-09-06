Here's a self-contained Python script that includes the function `filter_by_substring` which is designed to solve the problem you described:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the `contains` method to check if each string in the input list contains the given `substring`.