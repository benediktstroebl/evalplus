```python
from typing import List
def concatenate(strings: List[str]): 
    """Concatenate list of strings into a single string"""
    return ''.join(strings)
def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
    assert concatenate(['a', 'bc']) == 'abc'
    assert concatenate([None, 'a']) == 'a'
    assert concatenate([5]) == '5'
```
The code defines a function `concatenate` that takes a list of strings and concatenates them into a single string. It also comes a aspect test cases to verify the correctness of the `concatenate` function.