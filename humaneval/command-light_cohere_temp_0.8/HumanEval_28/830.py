```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(''.join(strings)
    )
def test_concatenate() -> None:
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['ab', 'bc']) == 'abc'
    assert concatenate(['abc']) == 'abc'
```
This code provides a function `concatenate` which takes in a list of strings and concatenates them into a single string, and a test function `test_concatenate` that verifies the correctness of the `concatenate` function by passing various test cases.