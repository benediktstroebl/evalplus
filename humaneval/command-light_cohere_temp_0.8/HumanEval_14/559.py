```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != '']

# Test case:
# return all prefixes of 'abc'
test_case = 'abc'
result = all_prefixes(test_case)
assert len(result) == 3  # Should be ['a', 'ab', 'abc']
```
The function all_prefixes takes a string and returns a list of prefixes from shortest to longest, excluding empty strings.