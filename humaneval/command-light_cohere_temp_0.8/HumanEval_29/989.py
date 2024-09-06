```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Test cases for the function
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"

result_test = filter_by_prefix(strings, prefix)
print(result_test)  # Output: ['abc', 'array']
```
This code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the filtering approach to iterate over the list of strings and check if each element starts with the given prefix. The resulting filtered list is then returned.