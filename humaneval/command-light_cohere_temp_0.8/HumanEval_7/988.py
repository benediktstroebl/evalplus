Here's the self-contained Python script with a function that filters an input list of strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the elements of the input list that contain the given substring. 

This is a self-contained solution that is both readable and effective for solving the problem.