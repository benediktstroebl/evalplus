Here is a self-contained Python script that defines a function **`filter_by_substring`** that filters an input list of strings for a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.lowercaseges(substring)]
```

This script provides a function that takes in a list of strings and a substring, and returns a new list of strings that contain the substring in a lowercase form. The function uses the lower() method to convert the substring to lowercase.