Here is a Python script that defines a function, `filter_by_prefix`, which filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix string as input and returns a new list that contains only the strings from the input list that start with the given prefix. 

It uses the `startswith` method from the string module to check if each string in the input list starts with the given prefix. 

This is a self-contained solution to the problem and passes the corresponding tests.