```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
test_cases = [
    [], 'a'
]
print("Test case 1: ", end='')
for idx, tc in enumerate(test_cases, 1):
    filtered = filter_by_prefix(tc, 'a')
    expected = ['a']
    print(f"{idx}. Expected: {expected}, Received: {filtered}")

test_cases = [
    ['abc', 'bcd', 'cde', 'array'], 'a'
]
print("\nTest case 2: ", end='')
for idx, tc in enumerate(test_cases, 1):
    filtered = filter_by_prefix(tc, 'a')
    expected = ['abc', 'array']
    print(f"{idx}. Expected: {expected}, Received: {filtered}")

test_cases = [['a', 'abc', 'bcda', 'z']]
print("\nTest case 3: ", end='')
for idx, tc in enumerate(test_cases, 1):
    filtered = filter_by_prefix(tc, 'a')
    expected = [['a', 'abc'])
    print(f"{idx}. Expected: {expected}, Received: {filtered}")
```

This script provides a filter_by_prefix function that accepts a list of strings and a prefix as input. The function then returns a list of all strings in the input list that start with the provided prefix. The test cases demonstrate the the expected behavior of the function.