The code is a filter function that takes a list of strings and a prefix as input and returns a new list of strings that match the given prefix. 

Here is the Python script:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script has a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that match the given prefix. The function uses the string.s.startswith method that checks if the of the given string, and returns `True` if the condition is met.