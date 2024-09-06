```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This code defines a function called `filter_by_substring` that filters a list of strings, `strings`, for a substring, `substring`. It utilizes the `find()` method from the string module to check if each string contains the `substring`.