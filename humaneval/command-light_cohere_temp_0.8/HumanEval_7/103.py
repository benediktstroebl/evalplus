```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python code defines a function named `filter_by_substring` that filters an input list of strings and returns a new list that includes only the elements that contain a given substring. The function uses the method `find` to search for the substring within each string, and the list comprehension `[]` to filter the strings accordingly.