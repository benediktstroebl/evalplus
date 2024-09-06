```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. 
This function is designed to solve the problem of filtering strings based on a given prefix, ensuring that it is self-contained and provides the expected output.