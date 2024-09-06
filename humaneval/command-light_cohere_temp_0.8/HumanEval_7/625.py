```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function called **filter_by_substring** that takes two parameters: a list of strings and a substring. It uses the simple list comprehension to iterate over the input strings and return a new list containing only the strings that contain the given substring.