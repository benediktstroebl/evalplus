```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Unit tests
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'a'
test_filter = [
    assert filter_by_prefix(strings, prefix) == ['abc', 'array'],
    assert not filter_by_prefix(strings, 'b')
]
test_no_prefix = [
    assert filter_by_prefix(strings, 'hello') == []
]
```
The above Python script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. The function returns a using list comprehension, and the tests assert that the function works as expected.