Here is a Python script that contains a self-contained function that filters out strings that do not contain the substring passed:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings that contains the given substring """
    return [string for string in strings if string.contains(substring)]
```

The function utilizes the contains method from string objects, which returns a boolean value indicating whether a given substring is present in the string. It then returns a filter the the input list of strings and returns a new list that contains only the strings that contain the given substring.