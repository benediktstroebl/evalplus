```python
from typing import List
def concatenate(strings: List[str]): 
    return ''.join(s.join(strings))

def test_concatenate():
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate([]) == ''
    assert concatenate(['']) == ''
    assert concatenate(['a', ' ', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'
```
The code defines a function called `concatenate` that takes a list of strings as an argument and returns the result of joining the strings into a single string using a comma as the separator. The code also provides a series of test cases to verify the correctness of the `concatenate` function.