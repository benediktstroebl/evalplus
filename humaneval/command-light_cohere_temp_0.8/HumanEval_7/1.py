Here is a self-contained Python script that defines a function `filter_by_substring` solving the problem of filtering an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The `filter_by_substring` function filters a list of strings and returns a new list containing only the strings that contain the given substring. 

In this script, we use the `contains` method to create a function and the `List` class from the typing module. We also use the regular expression containing the `contains` method to check if a string contains the substring.