```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This is achieved using a list comprehension, filtering strings based on the `startswith` method.

The behavior of the function is illustrated in the docstring, providing example inputs and showing the expected output. The code includes type annotations, helping to create clear documentation and enabling type checking tools.