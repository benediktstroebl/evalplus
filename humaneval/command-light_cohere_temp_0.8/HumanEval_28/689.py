```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The provided code defines a function **concatenate** that takes a list of strings and returns their concatenation. It also contains a verifying tests for the function correctness, passing all the test cases.