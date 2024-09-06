```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string] + all_prefixes(string[1:])
def all_prefixes_test(string: str) -> None:
    actual = all_prefixes(string)
    assert len(actual) == 3, f"Expected {len(string)}, got {actual}"
    assert actual[0] == 'a', f"Expected 'a', got {actual[0]} instead"
    assert actual[1] == 'ab', f"Expected 'ab', got {actual[1]} instead"
    assert actual[-1] == string[-1], f"Expected {string[-1]}, got {actual[-1]} instead"
all_prefixes_test('abc')
```