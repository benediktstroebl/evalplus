Here is a self-contained Python script that defines a function `filter_by_prefix` solving the problem you have described:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as parameters, and returns a new list containing only the strings from the input list that start with the given prefix. 

It uses the Python list comprehension with the `startswith` method to achieve this.