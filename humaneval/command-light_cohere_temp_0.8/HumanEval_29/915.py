Here is a Python script that includes a self-contained function to filter an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the using the type hint to indicate that the function will return a list of strings.

This code is self-contained and does not require any additional imports or external functions to be used.