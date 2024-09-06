```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '' and c not None]

# Test the function with an input string
test_string = "abc"
result = all_prefixes(test_string)
assert len(result) == 3  # Check the length of the result
assert [x for x in result if x != '' and x is not None] == ['a', 'ab', 'abc']  # Check if the result is as expected
```