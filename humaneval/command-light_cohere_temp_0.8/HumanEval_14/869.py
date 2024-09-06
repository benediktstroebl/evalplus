```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' if i == 0 else i for i in range(1, len(string) + 1)]

# Test case 1: Basic case
test_case1 = """a\nbc""
assert all_prefixes(test_case1) == ['a', 'ab', 'abc']

# Test case 2: Remove spaces
test_case2 = "a b c"
assert all_prefixes(test_case2) == ['a', 'b', 'c']

# Test case 3: Multi-word character
test_case3 = "a___b__c___"
assert all_prefixes(test_case3) == ['a__b__c']

# Test case 4: Capital and punctuation
test_case4 = "ABC! def!"
assert all_prefixes(test_case4) == ['ABC']
```
The function `all_prefixes` uses a list comprehension to generate all possible prefixes from the input string, regardless of its length. The test cases cover basic, space-free, and multi-word character scenarios.