```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1: Empty list
test_case1 = []
result = filter_by_substring(test_case1, 'a')
assert result == []

# Test case 2: Single string
test_case2 = ['abc']
result = filter_by_substring(test_case2, 'a')
assert result == ['abc']

# Test case 3: Multiple strings with substring
test_case3 = ['abc', 'bacd', 'cde', 'array']
result = filter_by_substring(test_case3, 'a')
assert result == ['abc', 'bacd']
```
This Python code defines a function called `filter_by_substring` that filters a list of strings for a given substring. The function uses the approach of iterating over each string in the input list and checking if the substring exists. The test cases demonstrate the simple usage of the function, passing different lists and substring values, and asserting the expected output.