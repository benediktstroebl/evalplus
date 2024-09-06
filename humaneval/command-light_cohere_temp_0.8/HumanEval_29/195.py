Here is a Python script with a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the specified prefix. 

This is a self-contained solution, which means that it can be used to filter strings in any list, as long as the list is passed into the function and the prefix is provided.