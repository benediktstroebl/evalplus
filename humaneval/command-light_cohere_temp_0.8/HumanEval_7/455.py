```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The code uses the method `contains` to check if each string in the list contains the substring, and the result is the list of strings that do contain the substring.