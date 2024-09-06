```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test cases for filter_by_prefix function
test_cases = [
    ['a', 'bcda'],
    ['abcde', 'array'],
    ['ab']
    ['abc', 'bcd'],
    ['abcd'],
    ['abcde', 'ab']
]


for item in test_cases:
    actual = filter_by_prefix(item, 'a')
    assert actual == ['abc', 'array'], f"incorrect result: {actual}"

test_passes = True
```

The provided Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function utilizes the `startswith` method to iterate through the strings in the list and returns only those that start with the specified prefix. The script provides a set of test cases that are used to validate the correctness of the `filter_by_prefix` function.