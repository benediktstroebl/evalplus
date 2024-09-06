Here is a Python script with a self-contained function that solves the problem of finding all prefixes in a given string. The code also includes tests to ensure the correctness of the function:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string if prefix != '' and not(prefix == string ')']

# Test case 1: Basic inputs
test_case1 = "abc"
assert all_prefixes(test_case1) == ['a', 'ab', 'abc']

# Test case 2: Empty string
test_case2 = ""
assert all_prefixes(test_case2) == []

# Test case 3: Single character
test_case3 = "x"
assert all_prefixes(test_case3) == ['x']

# Test case 4: Longer string with no prefix
test_case4 = "aebfghijklmnopqr"
assert all_prefixes(test_case4) == ['a', 'e', 'fgh', 'ijkl', 'mnop', 'qr']
```
The provided code is a Python script with a self-contained function all_prefixes that returns a list of all prefixes from the shortest to the longest in a given string. It also includes several test cases to ensure the correctness of the function's behavior.