```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

test_filter_by_substring = [
    TestCase(strings, []),
    TestCase(strings, ['abc', 'cde']),
    TestCase(strings, ['array']),
    TestCase(strings, ['hello'])
]

for test in test_filter_by_substring:
    print(test.contains(filter_by_substring(strings, substring)))
```