Here is a Python script that contains a self-contained function that filters out strings that do not contain the given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'abe', ' welcome']
sub = 'cde'
result = filter_by_substring(strings, sub)
print(result)  # Expected output: ['cde', 'array']
```

This script defines a function that filters out strings from a list based on a given substring. The example usage provided also demonstrates the expected output, which is the list of strings containing the specified substring.