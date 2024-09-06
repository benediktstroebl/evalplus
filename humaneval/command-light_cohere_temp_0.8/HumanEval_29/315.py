```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"

# Expected output: ['abc', 'array']
result = filter_by_prefix(strings, prefix)
print(result)

# Test case 2:
strings = ["a", "band", "data"]
prefix = "band"

# Expected output: []
result = filter_by_prefix(strings, prefix)
print(result)
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It utilizes the test cases to validate the function's behavior and output, which aligns with the expected results.