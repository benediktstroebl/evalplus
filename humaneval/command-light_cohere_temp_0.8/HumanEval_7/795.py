```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case with empty input list
test_empty_list = []
assert filter_by_substring(test_empty_list, 'a') == []

# Test case with non-empty list
test_list = ['abc', 'bacd', 'cde', 'array']
assert filter_by_substring(test_list, 'a') == ['abc', 'bacd', 'array']

# Test case with single string
test_single_string = 'abc'
assert filter_by_substring([test_single_string], 'a') == [test_single_string]

# Test case with substring present in list
test_substring = 'cde'
assert filter_by_substring([test_list], 'e') == ['cde']
```
This Python script provides a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses the uses a generator expression to iterate over the input list and checks if the given substring is present in each string. The test cases demonstrate the the expected behavior of the function with various inputs.