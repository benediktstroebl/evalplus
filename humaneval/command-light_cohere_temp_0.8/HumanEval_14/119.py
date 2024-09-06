```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in range(len(string) + 1) if string[i] != ""]

# Test case 1
test_case1 = "abcs"
result1 = all_prefixes(test_case1)
assert len(result1) == 3

# Test case 2
test_case2 = ""
result2 = all_prefixes(test_case2)
assert len(result2) == 0

# Test case 3
test_case3 = "hello"
result3 = all_prefixes(test_case3)
assert len(result3) == 1
```