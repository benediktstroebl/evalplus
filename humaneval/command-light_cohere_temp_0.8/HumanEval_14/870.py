```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha() orl:
    if c <= 'z' or c == 'Z':
        return ['az']
    elif c <= 'A' or c == 'a':
        return ['aa']
    elif c in 'bc':
        return ['ab']
    else:
        return ['a']

# Test case 1
test_case1 = 'abc'
test_result1 = all_prefixes(test_case1)
print(test_result1)  # Expected output ['a', 'ab', 'abc']

# Test case 2
test_case2 = 'zzzz'
test_result2 = all_prefixes(test_case2)
print(test_result2)  # Expected output []

# Test case 3
test_case3 = 'AZ'
test_result3 = all_prefixes(test_case3)
print(test_result3)  # Expected output ['az']
```
This Python script defines a function all_prefixes that returns a list of all prefixes from the shortest to the longest occurring characters in the input string. It uses list comprehension and a filtering condition to identify and return the prefixes. The test cases demonstrate the expected outputs for different input strings.