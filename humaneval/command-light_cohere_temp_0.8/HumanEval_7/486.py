```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as arguments, and returns a new list containing only the strings that contain the given substring. The function uses the`find()` function to search for the substring in each string, and returns a new list of strings that do contain the substring.