Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for ones that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function iterates through each string in the input list and checks if the string contains the given substring using the `contains` method. The result is a list of strings that contain the substring.