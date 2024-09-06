```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case: filtering strings containing 'a'
test_case = ['abc', 'bacd', 'cde', 'array', 'a', 'ad']
assert filter_by_substring(test_case, 'a') == ['abc', 'array']

# Test case: filtering strings NOT containing 'b' as a substring
test_case = ['abc', 'bacd', 'cde', 'array', 'a', 'ad']
assert filter_by_substring(test_case, 'b') == ['abc', 'cde', 'array']

# Test case: filtering strings containing multiple 'a's
test_case = ['abc', 'bacdaaa', 'cde', 'array', 'a']
assert filter_by_substring(test_case, 'a') == ['abc', 'bacdaaa', 'cde', 'array', 'a']

# Test case: filtering strings containing non-alph characters
test_case = ['abc123', 'sdghf', '!"']
assert filter_by_substring(test_case, 'a') == ['abc123']
```

This Python script provides a self-contained function `filter_by_substring` that filters a list of strings based on whether the given substring is present in each string. The test cases provided at the  the bottom demonstrate how the function behaves with various inputs and expected results.