Here's the provided self-contained Python function that filters an input list of strings for ones that contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```
This function accepts a list of strings and a substring as parameters, and returns a new list that contains only the strings from the input list that contain the given substring. 
In this version, the function is self-contained, which means it doesn't rely on any other functions or modules outside of itself, and can be fully understood and executed within the function itself.