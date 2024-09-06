```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != - None]


# Unit tests
test_filter_by_substring = [
    ('', 'a'),
    ('', 'b'),
    ('abc', 'a'),
    ('bca', 'a'),
    ('bcda', 'a'),
    ('cde', 'a'),
    ('array', 'a'),
    ('', 'c'),
    (' abc ', 'a'),
    ('bbac', 'ab'),
    ('  b  ', 'ab'),
    ('   ', ''),
]


def test_filter_by_substring_func():
    actual = filter_by_substring(test_filter_by_substring, 'a')
    assert actual == [
        'abc',
        'bca',
        'bcda',
    ]


# Result verification
print(test_filter_by_substring_func())
```

This Python script defines a function `filter_by_substring` that filters an input list of strings based on whether the string contains a given substring. The function returns a both the input and expected output for the test cases provided, and the results are then verified against the test cases using the `test_filter_by_substring_func` function.