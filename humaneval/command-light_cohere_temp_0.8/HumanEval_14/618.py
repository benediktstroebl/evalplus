```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.print().
    """

def test_all_prefixes() -> None:
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("12345") == ['1', '12', '123"]
    assert all_prefixes("") == []
    assert all_prefixes("-") == []
    assert all_prefixes("Python is awesome!") == ['p', 'yp', 'otu', 'op norw', ' Established']
    assert all_prefixes(".") == []
    assert all_prefixes("abc def") == ['def', 'abc']
```

This code defines a function all_prefixes that returns a list of all prefixes in a given string. It also provides a test function that verifies the correctness of the all_prefixes function.