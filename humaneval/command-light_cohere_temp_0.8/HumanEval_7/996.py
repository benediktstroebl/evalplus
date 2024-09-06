Here is a self-contained Python script that solves the problem of filtering strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the contains method to check if each string in the input list contains the given substring, and then returns a new list containing only those strings that do contain the substring. The function is also properly formatted and follows PEP 8 style guidelines.