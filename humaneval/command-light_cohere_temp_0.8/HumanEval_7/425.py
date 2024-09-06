Here's the self-contained Python function that implements the filter_by_substring function from the previous prompt:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The `contains` statement inside the function, along with the rest of the function body, is enclosed in a List comprehension, creating a fully self-contained solution to the given problem.

This function takes a list of strings and a substring as input, and returns a new list of strings from the input list that contain the given substring.