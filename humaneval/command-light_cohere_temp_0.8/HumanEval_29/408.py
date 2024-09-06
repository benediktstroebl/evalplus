```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
strings = ["abc", "bcd", "cde", "array", "Hello", "world"]
prefix = "array"
print(filter_by_prefix(strings, prefix))  # Output: ['array']
``` 
The code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filter the list of strings that start with the given prefix.