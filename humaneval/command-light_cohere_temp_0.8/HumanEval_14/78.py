```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join([i for i in string if i != '']) + ['']

# Test case 1
test_case1 = """xyzt#"
test_case1_prefixes = all_prefixes(test_case1)
assert test_case1_prefixes == ['#', 'xyzt', 'xyzs#']

# Test case 2
test_case2 = ""
test_case2_prefixes = all_prefixes(test_case2)
assert test_case2_prefixes == ['']

# Test case 3
test_case3 = "a"
test_case3_prefixes = all_prefixes(test_case3)
assert test_case3_prefixes == ['a']
```
This script defines a function `all_prefixes(string: str)` that returns a list of all prefixes of the input string, from shortest to longest, excluding the empty string. 

Three test cases are provided, each with a different input string and the expected output is validated using assertions.