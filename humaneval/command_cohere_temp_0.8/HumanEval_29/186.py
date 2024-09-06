```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. This is achieved using a list comprehension, filtering out elements that don't satisfy the condition `s.startswith(prefix)`.

To test this function, you can call it with different lists of strings and prefixes and check if it returns the expected results, as demonstrated below:
```python
# Test 1: Empty list, empty prefix
test_list = []
test_prefix = ''
expected_result = []

result = filter_by_prefix(test_list, test_prefix)

assert result == expected_result

# Test 2: List with one matching element, matching prefix
test_list = ['abc', 'bcd', 'cde', 'array']
test_prefix = 'a'
expected_result = ['abc', 'array']

result = filter_by_prefix(test_list, test_prefix)

assert result == expected_result

# Test 3: List with no matching elements, non-matching prefix
test_list = ['abc', 'bcd', 'cde', 'array']
test_prefix = 'z'
expected_result = []

result = filter_by_prefix(test_list, test_prefix)

assert result == expected_result
```

This way, the function's behavior is confirmed to align with the problem statement and yield the expected outcomes for different scenarios.