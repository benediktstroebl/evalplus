```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(*strings)

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate(['ab', 'a']) == 'abab'
    assert concatenate([123]) == '123'
```
This script defines a function `concatenate` that takes a list of strings and concatenates them into a single string. The `test_concatenate` function contains a series of test cases that validate the correctness of the `concatenate` function.