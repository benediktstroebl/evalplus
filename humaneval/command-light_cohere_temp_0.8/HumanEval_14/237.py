```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(i) for i in string if i != ""]

# Test case 1: Single character
test_case1 = "a"
assert all_prefixes(test_case1) == ["a"]

# Test case 2: Empty string
test_case2 = ""
assert all_prefixes(test_case2) == []

# Test case 3: Multiple characters
test_case3 = "abc"
assert all_prefixes(test_case3) == ["a", "ab", "bc"]
```

This script defines a function `all_prefixes` that returns a list of prefixes from the shortest to the longest of the input string. You can uncomment and run the script to test the function using various test cases.