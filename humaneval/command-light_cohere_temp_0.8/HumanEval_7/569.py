```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This script defines a function called `filter_by_substring` that uses the `contains` method to filter a list of strings based on whether the substring is present in each string.