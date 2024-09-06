```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case for function:
test_filter = [
    ['abc', 'bacd', 'cde', 'array', 'a'],
    ['cde', 'a']
]

expected_output = ['abc', 'bacd', 'array']

# Function call and assertion
assert filter_by_substring(test_filter, 'a') == expected_output, "Function failed the test case."
```