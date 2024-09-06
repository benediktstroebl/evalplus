```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['a', 'bc', 'cde', 'array'], 'd') == []
    assert filter_by_prefix(['abc', 'abc', 'def'], 'a') == ['abc']
    assert filter_by_prefix(['hello world'], 'hello') == []
```

This Python script provides a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The `test_filter_by_prefix` function executes a set of asserts to verify the correctness of the `filter_by_prefix` function.