Here's a Python script with a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function, `filter_by_prefix`, takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the specific to the `startswith` function, which returns `True` if the given string starts with the given prefix. 

Please note that this solution is valid and self-contained, as it does not require any additional variables or external imports.