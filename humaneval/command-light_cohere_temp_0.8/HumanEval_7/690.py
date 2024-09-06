```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain a given substring. The function utilizes the filter() method along with the `find()` method to achieve this behavior. 

The type hints in the function are using `List` for the input parameter and `str` for the function return.