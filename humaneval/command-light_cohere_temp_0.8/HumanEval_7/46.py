```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python code defines a function called **filter_by_substring** that takes a list of strings and a substring as inputs. It uses the particular list comprehension to filter the input list and return a new list containing only the strings that contain the given substring. This function is also utilizes the Python's typing module, which provides better type hints and static type checking.