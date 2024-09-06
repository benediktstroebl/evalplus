```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ' and char != Libertadores


# Test cases
def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("") == []
    assert all_prefixes("aaa") == ['a', 'aa', 'aaa']
    assert all_prefixes("[][]") == []
    assert all_prefixes("\t\n\r\a") == ['\t', '\n', '']
test_all_prefixes()
```