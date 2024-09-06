Here's a self-contained Python script with a function that filters an input list of strings for a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a `filter_by_substring` function that takes a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. 
The function utilizes the list comprehension with the `contains` method to achieve this.