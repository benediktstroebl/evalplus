Here's the solution to the problem using the provided function `filter_by_substring`:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the `contains` method from the string module to check if each string contains the given `substring`. The function returns a new list containing only the strings that contain the given substring.

Please note that the function uses the `typing` module, which is not a standard library and might require additional dependencies. You can add the goal to solve the problem with any other strings or substring variations.