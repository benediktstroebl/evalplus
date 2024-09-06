Here's a self-contained Python script that implements the function `filter_by_substring` as described:

```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function that filters a list of strings, returning a new list containing only the strings that contain the given substring. It uses the specific type hints (like `List[str]` and `contains`) to ensure the function's signature is correct.