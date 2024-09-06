Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the single string in the input list and the given prefix, and returns a new list that contains the single matching string. 

The function is designed to be easy to understand and to be efficient.