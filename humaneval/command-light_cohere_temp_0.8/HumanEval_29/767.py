```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ['abc', 'bcd', 'cde', 'hello', 'world! slowest', 'array']
prefix = 'a'

# Function call
result = filter_by_prefix(strings, prefix)

print("Result:", result)

if len(result) != 2:
    raise ValueError("Error: function doesn't return expected output.")
```