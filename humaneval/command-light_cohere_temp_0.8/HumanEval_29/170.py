```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['b', 'de'], 'a') == []
```  This Python code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the tests with a list of strings and a prefix, it iterates over each element in the list. The `assert` statements at the test_filter_by_prefix() function to verify the correctness of the `filter_by_prefix` function.