Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function uses a list comprehension to filter the strings in the input list, only keeping those that start with the given prefix. It uses the string.value is a value of the function is the list of strings, and the prefix is the string passed in as an argument. The function then returns a filtered list of strings that start with the given prefix.