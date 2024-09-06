```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "1234"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print the result
print(result)
```