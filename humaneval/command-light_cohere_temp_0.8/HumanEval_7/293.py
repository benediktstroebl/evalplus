```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only those strings that contain a given substring. The function utilizes the particular to iterate through the list and check whether each string contains the substring, effectively filtering out any strings that don't contain the substring. The function is designed with type hints to improve code clarity and maintain good practice.