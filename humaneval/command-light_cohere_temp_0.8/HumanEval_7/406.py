```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
#Unit tests
strings = ["abc", "bacd", "cde", "array", "hello"]
sub = "a"

test_filter_by_substring = [
    "Test 1: Should return ['abc', 'bacd'] given strings: ['abc', 'bacd', 'cde', 'array'] and substring: 'a'."
]

test_filter_by_substring. [
    "Test 2: Should return [] given empty strings."
]
test_filter_by_substring. [
    "Test 3: Should return ['array'] given strings: ['abc', 'bacd', 'cde', 'array'] and substring: 'array'."

print('Result of test 1: ', end='')
print(test_filter_by_substring)

print('\nResult of test 2: ', end='')
print(test_filter_by_substring)

print('\nResult of test 3: ', end='')
print(test_filter_by_substring)
```