```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This code defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list that contains only the strings that contain the given substring. 

The function uses a list comprehension to iterate over the input strings and check if each string contains the given substring. 

This solution efficiently filters the input list based on the given substring, making it a self-contained and concise way to solve this problem in Python.