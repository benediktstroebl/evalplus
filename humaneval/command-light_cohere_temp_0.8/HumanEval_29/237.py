Here is a self-contained Python script that defines a function `filter_by_prefix` that filters an input list of strings based on their prefix:
```python
from typing import List
import re

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    patterns = [f"{prefix}{c}" for c in strings]
    return [s for s in strings if re.search(patterns[0], s)]
```

This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix as input, and returns a new list of strings that match the given prefix. The function uses the pattern matching with the `re.re string that starts with the prefix, then it is added to the output list.

For example, if you pass the list of strings ['abc', 'bcd', 'cde', 'array'] and the prefix 'a', the function will return the strings ['abc', 'array'].