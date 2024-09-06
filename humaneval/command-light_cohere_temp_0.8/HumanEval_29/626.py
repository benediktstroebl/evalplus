```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases
test_data = [
    ['abc', 'bcd', 'cde', 'array', 'begin'],
    ['xx', 'xxy', 'xxz'],
    ['https://www. saw']

def test_filter_by_prefix():
    actual = filter_by_prefix(test_data['a'], 'a')
    assert actual == ['abc', 'array']

    actual = filter_by_prefix(test_data['b'], 'x')
    assert actual == ['xx', 'xxy']

    actual = filter_by_prefix(test_data['c'], 'xx')
    assert actual == ['xxz']

    with pytest.assert():
        actual, assert actual == []
```