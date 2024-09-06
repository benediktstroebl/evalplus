```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix`, which takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the specified prefix. The function uses the string `startswith` to check if each string in the input list starts with the provided prefix. The `filter_by_prefix` function is a good self-contained solution to the problem of filtering strings based on a given prefix.