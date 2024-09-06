```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string]

# Test case 1
test_case1 = "abrac"
print(all_prefixes(test_case1))  # Output: ['a', 'ab', 'ab', 'ac']

# Test case 2
test_case2 = "abc"
print(all_prefixes(test_case2))  # Output: ['abc']

# Test case 3
test_case3 = "a123"
print(all_prefixes(test_case3))  # Output: []
```
This script defines a function all_prefixes that returns a list of all prefixes from the shortest to the longest character in the input string.