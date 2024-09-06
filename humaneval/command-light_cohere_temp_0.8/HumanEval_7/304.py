Here's a self-contained Python function that filters an input list of strings for ones that contain a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function iterates through each string in the input list and checks if the string contains the provided substring using the `contains` method.