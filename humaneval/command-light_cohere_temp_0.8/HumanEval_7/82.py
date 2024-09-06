```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This code defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses the use a `contains` to iterate over each string and check if the string contains the given substring using the `contains` method. The function returns a string that contains the substring.