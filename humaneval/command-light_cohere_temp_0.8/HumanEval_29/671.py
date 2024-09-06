```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    test_strings = ['abc', 'bcd', 'cde', 'a', 'array', 'begin', 'fish', 'hello']
    expected = ['abc', 'array', 'begin']
    actual = filter_by_prefix(test_strings, 'a')
    assert actual == expected


if __name__ == "__main__":
    test_filter_by_prefix()
```
This code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list that contains elements that start with the given prefix. The `test_filter_by_prefix` function is designed to test the `filter_by_prefix` function by passing the test strings and expected output. The `__main__` block is where the test function is called to validate the function's correctness.