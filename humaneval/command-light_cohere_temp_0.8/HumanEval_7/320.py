```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code defines a function called **`filter_by_substring`** that filters a list of strings to only include those that contain a given substring. The function uses the search method **`find`** to check if each string in the list contains the given substring, and returns a new list containing only the matching strings.