```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case with a list of strings and a substring
test_case = [
    "abc", "bacd", "cde", "array"
]
substring = "a"

result = filter_by_substring(test_case, substring)

assert result == ['abc', 'bacd', 'array']
```
This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It then provides a test case with a list of strings and a specific substring, and asserts the result of the function call to be the expected output.