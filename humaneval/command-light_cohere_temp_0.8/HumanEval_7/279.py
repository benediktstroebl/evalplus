```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code defines a function called `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. 

The code uses the list comprehension to filter the strings that contain the given substring, and the type of the input parameters is defined using the `typing` module.