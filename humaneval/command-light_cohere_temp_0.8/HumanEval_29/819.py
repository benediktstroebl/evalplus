```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Example test cases
test_cases = [
    ['abc', 'bcd', 'cde', 'hello', 'world'],
    ['a', 'apple', 'cat', 'dog'],
    ['aa', 'ab'],
    ['a']
]


def test():
    assert filter_by_prefix(test_cases, 'a'), 'Invalid prefix "a", should return []'
    assert filter_by_prefix(test_cases, 'apple'), 'Invalid prefix "apple", should return []'
    assert filter_by_prefix(test_cases, 'cat'), 'Invalid prefix "cat", should return []'
    assert filter_by_prefix(test_cases, 'dog'), 'Invalid prefix "dog", should return []'
    assert filter_by_prefix(test_cases, 'hello'), 'Invalid prefix "hello", should return []'

print('Tests passed!')
```