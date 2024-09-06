```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and including only those that contain the substring `substring`. This is indicated by the inclusion of the `in` operator, which checks for membership.  This approach allows the function to efficiently filter through the list and retrieve the desired strings.  By utilizing Python's typing module, the function includes type annotations, specifying that `strings` is a list of strings and `substring` is a single string, which enhances code readability and maintainability.