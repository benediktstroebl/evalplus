```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python code defines a function called `filter_by_substring` that filters an input list of strings to include only those that contain a given substring. It uses the particular to search for the substring within each string in the list and returns a new list containing only the strings that contain the substring. The code is using the `find` function to search for the substring within the strings.