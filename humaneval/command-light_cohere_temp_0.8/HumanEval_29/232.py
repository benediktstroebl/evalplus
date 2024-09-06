```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Test cases
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"

print("Test 1 Result:", filter_by_prefix(strings, prefix))

print("Test 2 Result:", filter_by_prefix([12, 123, 124], prefix))

print("Test 3 Result:", filter_by_prefix([abc, bcd, cde], 'cd'))
```
This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It returns a use the specific test cases to verify the function's behavior.