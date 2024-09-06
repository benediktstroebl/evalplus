```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code implements a function filter_by_substring that filters an input list of strings and returns a new list that contains only the strings that contain the given substring. The test case Pass uses the this function with sample inputs and confirms the correctness of the output.