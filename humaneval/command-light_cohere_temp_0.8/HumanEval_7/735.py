```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function that filters an input list of strings to only include those that contain a given substring. The function utilizes the string.simple and list comprehension to achieve this task. The test cases are included in the code to ensure the function's correctness.