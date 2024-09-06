```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "cde", "bca", "cce", "array", "a"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Test if function call returns correct result
print(result == strings)
```