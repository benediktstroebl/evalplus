```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code defines a function `filter_by_substring` that takes two parameters: a list of strings and a substring. The function returns a filter the strings list by checking if each string contains the given substring using the `contains` method.