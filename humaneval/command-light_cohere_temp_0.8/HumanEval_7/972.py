```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a `filter_by_substring` function that takes in a list of strings and a substring as parameters, and returns a new list that contains only the strings from the input list that contain the given substring. 

The script then uses the `contains` statement to print the function's output, which is the new list that only contains the strings that contain the given substring.