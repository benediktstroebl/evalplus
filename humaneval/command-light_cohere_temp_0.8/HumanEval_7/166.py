```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code you provided is a Python script that contains a function `filter_by_substring` that filters an input list of strings to only include those that contain a given substring. The function uses the the type hint to indicate the expected input types for the function parameters.