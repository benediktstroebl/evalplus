Here's the function that filters the strings in the markdown code block:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list of strings and a prefix as input. It returns a filtered list, which contains only the strings from the input list that start with the given prefix. This is an good way to the given problem and passes the test of being able to filter a list of strings based on a given prefix.