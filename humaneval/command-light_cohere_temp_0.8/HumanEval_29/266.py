Here is a Python script with a self-contained function that solves the problem of filtering strings based on their prefixes:
```python
from typing import List
import re


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if re.search(prefix, s)]


# Test cases
test_cases = [
    ['abc', 'bcd', 'cde', 'array'],
    ['foo', 'bar', 'baz'],
    ['abc', 'a', 'b'],
    ['a']
]


for test_case in test_cases:
    print(filter_by_prefix(test_case, 'a'), ' => ', end='')
    print('', end='')
    print(filter_by_prefix(test_case, 'b'), ' => ', end='')
    print('')
```
The above script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It then provides several test cases to test the function. The function uses the re.0 to check if a strings in the input list start with the specified prefix.