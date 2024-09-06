```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python script defines a function filter_by_prefix that takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. The function uses the operator [] and the Python list comprehension to filter the input list based on the condition that the string starts with the given prefix.