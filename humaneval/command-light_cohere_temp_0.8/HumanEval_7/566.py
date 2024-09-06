Here's a self-contained Python script with a function that filters strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The provided function filters a list of strings and returns a new list containing only the strings that contain the given substring. 

The function utilizes the `find()` method to search for occurrences of the substring within each string.