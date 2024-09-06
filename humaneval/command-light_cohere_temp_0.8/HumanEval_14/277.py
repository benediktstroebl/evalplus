```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [i for i, char in enumerate(string, 1) if char.isalpha()]
isalpha()

# Test case: Return all prefixes for "hello"
test_case = "hello"
result = all_prefixes(test_case)
assert len(result) == 6
result2 = all_prefixes(" World ")
assert result == result2  # Should be true due to memoization
```