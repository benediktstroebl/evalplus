```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The function `filter_by_substring` filters a list of strings and returns only the ones that contain the given substring. It utilizes the using a list comprehension with the `contains` built-in function `contains` to achieve this.