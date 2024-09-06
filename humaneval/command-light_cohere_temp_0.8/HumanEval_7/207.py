```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python code defines a function `filter_by_substring` that filters an input list of strings and returns a new list that includes only those elements that contain a given substring. 

The function utilizes the `find()` method with the `substring` parameter to check if each string in the input list contains the substring. 

The code is self-contained and effectively solves the task of filtering strings that contain a specific substring.