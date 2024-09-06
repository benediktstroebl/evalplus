Here's the self-contained Python script with the function `filter_by_substring` that solves the problem of filtering strings for a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This function uses the `find()` method from the string module to check if each string contains the given substring. The function returns a list of all the strings from the input list that contain the substring.