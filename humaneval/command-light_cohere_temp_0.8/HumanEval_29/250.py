```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test case 1: Filter strings that start with 'a'
test_case_1 = [ 'abc', 'bcd', 'cde', 'array' ]
test_case_1_expected = ['abc', 'array']
test_case_1_result = filter_by_prefix(test_case_1, 'a')
assert test_case_1_expected == test_case_1_result

# Test case 2: Filter strings that start with 'xx'
test_case_2 = [ 'abc', 'bcd', 'cde', 'xx' ]
test_case_2_expected = ['xx']
test_case_2_result = filter_by_prefix(test_case_2, 'xx')
assert test_case_2_expected == test_case_2_result

# Test case 3: Filter strings that start with '' (should return everything)
test_case_3 = ['abc', 'bcd', 'cde', '123']
test_case_3_expected = ['abc', 'bcd', 'cde', '123']
test_case_3_result = filter_by_prefix(test_case_3, '')
assert test_case_3_expected == test_case_3_result
```
The function `filter_by_prefix` takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the specified prefix. The test cases demonstrate that function by filtering different lists of strings with different prefixes. The test cases pass, so the function is working correctly.