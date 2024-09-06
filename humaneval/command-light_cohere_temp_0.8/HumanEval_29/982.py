```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function `filter_by_prefix` that filters an input list of strings, returning only those that start with a specified prefix. 

The function uses the typing module for better string formatting and type hinting. The function takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the provided prefix.