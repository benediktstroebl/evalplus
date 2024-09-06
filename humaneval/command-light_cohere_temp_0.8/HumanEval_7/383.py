Here's a Python script with a self-contained function that filters an input list of strings based on a substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. 
The function uses the `find()` method to check if each string in the list contains the given substring.