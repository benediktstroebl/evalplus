```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'bd', 'cd', 'abe', 'array'], 'b') == ['abc', 'abe']
    assert filter_by_prefix(['xray', 'td', 'seg'], 'seg') == []
``` 
This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with that particular prefix. The `test_filter_by_prefix` function tests are added to demonstrate the functionality of the `filter_by_prefix` function.