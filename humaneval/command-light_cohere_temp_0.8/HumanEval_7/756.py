Here is a Python script that contains a self-contained function that filters an input list of strings for a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function, `filter_by_substring`, takes a list of strings and a substring as input. It returns a
a new list containing only the strings from the input list that contain the given substring.

For example, if you input the list `['abc', 'bacd', 'cde', 'array']` and the substring `a`, the output will be `['abc', 'bacd']`.