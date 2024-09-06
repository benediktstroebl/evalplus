```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.array(string) if prefix]

# Test case: Get all prefixes of "abc"
test_case = "abc"
result = all_prefixes(test_case)
assert len(result) == 3  # Check the length of result is 3
assert result == ['a', 'ab', 'abc']  # Check the result is ['a', 'ab', 'abc']
print("Passed all tests!")
```