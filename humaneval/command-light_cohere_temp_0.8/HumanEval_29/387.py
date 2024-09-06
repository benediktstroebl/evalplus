Here is a self-contained Python script that defines a function `filter_by_prefix` solving the problem of filtering strings by their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This function takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. It uses the generating a list comprehension to filter the strings by their prefix.

The function is then tested with various input strings and prefixes.