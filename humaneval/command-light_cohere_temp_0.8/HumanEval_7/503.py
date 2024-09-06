```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list of strings that contain the given substring. The function uses the main logic: it iterates over each string in the input list, and checks if the string contains the given substring using the `contains` method. The result is a list comprehension, which creates a new list containing only the strings that contain the substring.