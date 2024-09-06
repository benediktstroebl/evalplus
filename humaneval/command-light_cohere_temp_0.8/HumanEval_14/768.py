```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string, 1)]

# Test case 1
test_case1 = "abc"
assert all_prefixes(test_case1) == ['a', 'ab', 'abc']

# Test case 2
test_case2 = "fpsst!"
assert all_prefixes(test_case2) == ['f', 'fs', 'fps', '!' ]

# Test case 3
test_case3 = "  # this is longer than 3 characters
"""
assert all_prefixes(test_case3) == ['']
```
This script defines a function all_prefixes that returns a list of all prefixes in a given string, starting from the shortest to the longest.  The test cases demonstrate the validation of the function. You can add more test cases to further validate the function.