Here is a Python script with a self-contained function that solves the problem and passes the tests:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function, `filter_by_prefix`, which takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. 

It uses the `startswith` method to filter and create a new list. 

The `typing` module is imported to the code to provide type hinting and better documentation.