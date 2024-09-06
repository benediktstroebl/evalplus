```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The provided Python script defines a function `filter_by_substring` that filters an input list of strings to only include those that contain a given substring. 

This function uses the `find()` method to search for the substring in each string, and then returns a new list containing only the strings that contain the substring. 
This is a self-contained solution that can be used to solve the given problem, which is to filter a list of strings for those that contain a given substring.