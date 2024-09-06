Here is a self-contained Python script with a function that filters an input list of strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script provides a well-organized and self-contained solution to the problem you have described. The function uses the filtering approach to return a new list containing only the strings that contain the given substring. 

The `contains` type hint helps in making the function's return more explicit and gives clarity to the function's return type.