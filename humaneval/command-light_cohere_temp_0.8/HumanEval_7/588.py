Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes a list of strings and a substring as input, and returns a new list that contains only the strings that contain the given substring. The function uses the ** contains** to check if a string contains the substring, which is a built-in Python method.