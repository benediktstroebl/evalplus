```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix`, which takes a list of strings and a prefix as input and returns a new list of strings that start with the given prefix. It uses the method `list.strip` for the fact that all strings that start with the given prefix, which the function then passes the test.