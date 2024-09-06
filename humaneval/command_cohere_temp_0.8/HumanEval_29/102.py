```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate over each string in the input `strings`, and checks if it starts with the specified `prefix`, using the `startswith` method. If a string starts with the prefix, it's included in the resulting list.