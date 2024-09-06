```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The code defines a function **filter_by_prefix** that takes in a list of strings and a prefix as input. It uses the general list comprehension to filter the list and returns a new list that contains only the strings that start with the given prefix. This function is easy to read and understand, is self-contained, and can be used to solve the problem of filtering strings that start with a given prefix.