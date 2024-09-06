Here is a Python script that contains a self-contained function that solves the problem of filtering an input list of strings that contain a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The `filter_by_substring` function takes a list of strings and a substring as input and returns a new list that contains only the strings from the input list that contain the given substring. 

This function uses the `contains` method to check if each string in the input list contains the given substring.