Here is a Python script with a self-contained function that solves the problem of filtering strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring]
```

Here, the function filters and returns only the strings that contain the given substring.