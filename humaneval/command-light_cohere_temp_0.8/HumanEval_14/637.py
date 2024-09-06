```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string]

# Test case: Create list of all prefixes from shortest to longest of the string
test_prefixes = ['abc', 'a', 'ab', 'abc']
assert all_prefixes('abc') == test_prefixes

# Another test case: Should work without any exceptions!
try:
    all_prefixes('abc')
except Exception as e:
    print(f"Exception occurred: {e}")
```