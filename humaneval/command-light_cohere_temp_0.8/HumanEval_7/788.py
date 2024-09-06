```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python code defines a function called **filter_by_substring** that filters a list of strings and returns a new list containing only the elements that contain a given substring. 

The function uses the list comprehension to iterate through the input strings and checks if each element contains the specified substring.