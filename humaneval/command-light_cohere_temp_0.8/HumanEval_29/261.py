```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix."""
    return [string for string in strings if string.startswith(prefix)]


# Test the function with sample inputs and expected outputs
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"
expected = ["abc", "array"]
print(filter_by_prefix(strings, prefix), "Expected:", expected)
```