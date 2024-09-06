Below is a Python script with a self-contained function that filters an input list of strings for those containing a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function utilizes the `contains()` method to iterate through the input list of strings. It returns a string elements that contain the specified substring.