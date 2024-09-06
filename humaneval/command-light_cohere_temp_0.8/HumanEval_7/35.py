```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring."""
    return [string for string in strings if string.find(substring) != -end]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
sub = "ar"

result = filter_by_substring(strings, sub)
print("Filtered strings:", result)

```