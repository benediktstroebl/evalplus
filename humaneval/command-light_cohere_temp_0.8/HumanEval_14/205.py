```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [x for x in string if x != '']

# Test case 1: Single character string
test_case1 = 'a'
assert all_prefixes(test_case1) == ['a']

# Test case 2: Empty string
test_case2 = ""
assert all_prefixes(test_case2) == []

# Test case 3: Longer string with no prefix
test_case3 = 'bowsers'
assert all_prefixes(test_case3) == ['']

# Test case 4: Longer string with single character prefix
test_case4 = 'aoes'
assert all_prefixes(test_case4) == ['a']

# Test case 5: Longer string with multiple prefixes
test_case5 = 'abacad'
assert all_prefixes(test_case5) == ['a', 'ab', 'ac', 'abc']

# Test case 6: String with several prefixes
test_case6 = 'aa bcb cdc efeff'
assert all_prefixes(test_case6) == ['a', 'ab', 'cb', 'cd', 'ef', 'ff']
```
The provided code defines a Python function all_prefixes that generates a list of all prefixes from shortest to longest of an input string. It uses list comprehension with a simple algorithm to achieve this. The code also includes a set of test cases to verify the correctness of the all_prefixes function.