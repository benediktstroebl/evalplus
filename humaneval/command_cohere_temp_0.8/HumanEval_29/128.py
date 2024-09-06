```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate through each string in the input list and check if it starts with the provided prefix using the `startswith` method. If a string starts with the prefix, it's included in the resulting list. If it does not, it's excluded from the list. 

The function is designed to be self-contained, meaning it can be dropped into any Python project, and it will work as expected without relying on external dependencies. 

To ensure the function works correctly for different scenarios, you may want to add tests to validate its behavior. Below is a markdown code block with example tests for the `filter_by_prefix`:
```python
# Tests:
assert filter_by_prefix([], 'a') == []
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar') == ['array']
assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ab') == ['abc']
```