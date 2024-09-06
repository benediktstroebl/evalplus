Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings that start with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix.