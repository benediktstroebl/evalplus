```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python script defines a function `filter_by_substring` that filters an input list of strings based on whether each string contains a given substring. It utilizes the Python's `find()` method to search for the substring within each string, and then returns a new list containing only the strings that contain the substring. 

The function is self-contained and efficient, making it suitable for solving real-world problems like filtering a list of strings for a specific pattern.