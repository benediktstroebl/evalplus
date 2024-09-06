```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings for the presence of a substring."""
    return [x for x in strings if substring in x]

# Test the function with different inputs
strings = ["abc", "hello", "world", "!flat", "hello world"]
sub = "hell"
result = filter_by_substring(strings, sub)
print(result)  # Output: ['hello', 'world']
```