```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. 

To achieve this, it uses a list comprehension, iterating over each string in `strings`, and checking if it starts with the `prefix` using the `startswith` method.