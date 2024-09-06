```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with several inputs and assertions
strings = ["abc", "bacd", "cde", "array", "xyz"]
sub = "a"

# Expected output: ['abc', 'bacd', 'array']
result = filter_by_substring(strings, sub)

assert len(result) == 3, "Invalid output length"

assert sub in result[0], "Invalid result, missing expected substring"

assert result[1] == 'bacd', "Invalid result, incorrect matching"

assert result[2] == 'array', "Invalid result, incorrect matching"
```
This script defines a function `filter_by_substring` that filters a list of strings for a given substring. It tests the specific inputs and assertions to ensure the function's correctness with various scenarios.