Certainly! Here is a self-contained Python script that defines and executes a function `filter_by_prefix` which accepts a list of strings and a prefix as arguments and returns a new list containing only the strings that start with that given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function uses a list comprehension to iterate through each string in the input list. It uses the basic condition to check if the string starts with the given prefix, which is done using the `startswith` method.