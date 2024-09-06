```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This code provides a way to filter a list of strings by their prefix. It uses the Python's List and str types and creates a function called `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with that prefix. 

The code uses the Python in-line list comprehension to filter out the strings that start with that prefix from the input list.