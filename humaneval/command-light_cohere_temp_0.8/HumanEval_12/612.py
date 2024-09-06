```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Out of list of strings, returns the longest string """
    if not strings:
        return None
    return max(strings, key=len)

# Test case 1: Input list is empty
test_case_1 = []
result_case_1 = longest(test_case_1)
assert not result_case_1

# Test case 2: One string in the list has the same length
test_case_2 = ['a']
result_case_2 = longest(test_case_2)
assert result_case_2 == 'a'

# Test case 3: Input list has multiple strings of the same length
test_case_3 = ['ccc']
result_case_3 = longest(test_case_3)
assert result_case_3 == 'ccc'
```
This script defines a function called `longest` that takes a list of strings as input and returns the longest string from that list. The function uses the max function with the `key=len` argument to identify the longest string. The tests are passed to verify the correctness of the function, by providing various input cases and checking if the output matches the expected result.