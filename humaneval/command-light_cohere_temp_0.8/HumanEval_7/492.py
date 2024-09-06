Here's the solution to the markdown code block problem:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function iterates through each string in the input list and returns a new list containing only those strings that contain the given substring. The function is a most straightforward and self-contained, solving the problem of filtering strings that contain a given substring.