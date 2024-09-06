Here is a self-contained Python script with a function that filters an input list of strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
The script provides a function to filter an input list of strings, the strings list, and return a new list that contains only the elements of strings that contain the given substring.