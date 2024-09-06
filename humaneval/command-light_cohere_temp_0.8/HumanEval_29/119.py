```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Run the function's tests
def test_filter_by_prefix() -> None:
    assert filter_by_prefix([], 'a'), " failing test: expected ['a'] but got an empty list"
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), " failing test: expected ['abc', 'array'] but got ["cde"]"

# main code
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
print(filter_by_prefix(strings, prefix))
```