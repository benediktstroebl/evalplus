```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases
test_cases = [
    [], ['a'], ['abc'], ['a', 'bcd'], ['cde', 'abc']
]

for test_case in test_cases:
    actual_result = filter_by_prefix(test_case, 'a')
    assert actual_result == ['a', 'abc'], f"Error in test case: {test_case}"

test_cases = [
    [], ['bcd', 'cd'], ['cd', 'cdca'], ['cd', 'cd'], ['cd', 'cd']
]

for test_case in test_cases:
    actual_result = filter_by_prefix(test_case, 'b')
    assert actual_result == ['bcd', 'cd'], f"Error in test case: {test_case}"
```
The code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the specified prefix. The test cases help to verify the correctness of the `filter_by_prefix` function by passing different lists of strings and prefixes and checking if the filtered result matches the expected output.