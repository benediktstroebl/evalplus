```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(). string(string[i:]) for i in range(1, len(string)) if string[i-1] != '']

# Test case 1: Simple string with single prefix
test_case1 = """abcd"""
assert all_prefixes(test_case1) == ['ab']

# Test case 2: String with multiple prefixes
test_case2 = "abc"
assert all_prefixes(test_case2) == ['a', 'ab', 'abc']

# Test case 3: Empty string
test_case3 = ""
assert all_prefixes(test_case3) == []

print("All prefixes successfully validated!")
```