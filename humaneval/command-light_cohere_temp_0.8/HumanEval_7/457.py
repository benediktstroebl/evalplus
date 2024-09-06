```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python code defines a function called **filter_by_substring** that filters an input list of strings and returns a new list containing only the strings that contain a given substring. The function uses the string slicing and the find() method to search for the substring within each string in the list.