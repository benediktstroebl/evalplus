```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate over each string in `strings` and returns the ones that start with the `prefix`. This is done using the `startswith` method. It returns a list of those matching strings. 

The function is self-contained, meaning it does not rely on any external variables or functions defined outside of its scope. It can be used independently as a standalone function in other projects.  It is also concise, clear, and easy to understand, following Python's style guidelines, specifically the PEP 8 style guide, making it ergonomic and optimized for readability and maintainability.