```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and including only those strings that contain the substring `substring`. This is indicated by the inclusion of the `substring` in each string, which is checked using the `in` operator.  This provides a concise way to filter the list according to the given criteria.  This solution directly addresses the problem statement, providing a clear and efficient implementation.  By using typing annotations and applying the function to example scenarios, we also ensure better code readability, maintainability, and robustness.  This contributes to a more comprehensive and understandable solution.