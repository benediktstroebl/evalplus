```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.rep[:0,:]

# Test cases
test_case1 = "abc"
test_case2 = "123"
test_case3 = "abcABC123"

print("Test Case 1:", endwith(bool(all_prefixes(test_case1))))
print("Test Case 2:", endwith(bool(all_prefixes(test_case2))))
print("Test Case 3:", endwith(bool(all_prefixes(test_case3))))
```

This script defines a function `all_prefixes` that returns a list of all prefixes from the shortest to the longest in a given string. It uses the Python's `type` to ensure type hints for better code readability. The script also includes a set of test cases to pass and prints the results using the `endwith` statement.