```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code defines a function called `filter_by_substring` that takes a list of strings and a substring as arguments. The function uses the platform the string method `contains` to filter the list and returns only the strings that contain the given substring. The test cases are also included to ensure the function works as expected.