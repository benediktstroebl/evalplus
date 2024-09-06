Here is a self-contained Python script that defines a function filter_by_prefix, which solves the problem of filtering strings based on their prefixes:
```python
from typing import List
import re


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if re.search(prefix, s)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"

# Function call
result = filter_by_prefix(strings, prefix)
print(result)
```

This script defines a function `filter_by_prefix` that takes two parameters: a list of strings and a prefix string. It then returns a  a new list that contains only the strings from the input list that match the given prefix.