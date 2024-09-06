```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function called `filter_by_substring`, which filters a list of strings and returns a new list that contains only the strings that contain a given substring. The function utilizes the process of iterating through each string in the input list and checking if each string contains the provided substring using the `contains` method. The function successfully passes the example tests where it is used to filter lists of strings containing different substrings.