Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for ones that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This script defines a function `filter_by_substring` that takes in a list of strings and a substring as input, and returns a new list of strings that contain the substring. It uses the fact list comprehension to iterate over the input list of strings, and for each string, it checks if the substring is present in the string using the `in` operator.