```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i, char in enumerate(string, 1)]

# Test case 1
test_case1 = "abcs"
print(all_prefixes(test_case1))  # Output: ['a', 'ab', 'acs']

# Test case 2
test_case2 = "abc"
print(all_prefixes(test_case2))  # Output: ['abc']

# Test case 3
test_case3 = "xyabc"
print(all_prefixes(test_case3))  # Output: ['xyab', 'abc']
```
This code defines a function called `all_prefixes` that returns a list of all prefixes in the input string. It uses a specific character to iterate over each character in the string from shortest to longest.