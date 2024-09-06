```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function uses the List comprehension technique to filter a list of strings based on whether the string contains a given substring. It takes a str substring and returns a new list containing the strings from the input list that do contain the given substring. 

The function is self-contained and effectively solves the problem of filtering strings based on the presence of a substring.