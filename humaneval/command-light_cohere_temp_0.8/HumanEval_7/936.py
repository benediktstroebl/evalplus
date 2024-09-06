```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case with empty list
test_empty = []
result = filter_by_substring(test_empty, 'a')
assert result == []

# Test case with strings containing substring
test_strings = ['abc', 'bacd', 'cde', 'array', 'anderson', 'a']
result = filter_by_substring(test_strings, 'a')
assert result == ['abc', 'bacd', 'array']

# Test case with strings not containing substring
test_strings = ['abc', 'dgd', 'cde', 'anderson', 'far']
result = filter_by_substring(test_strings, 'a')
assert result == []
```

This Python code defines a function `filter_by_substring` that filters a list of strings for a given substring. The function uses a filtering technique to iterate through the input list of strings and returns only the strings that contain the specified substring. The code also includes several test cases to validate the behavior of the `filter_by_substring` function: