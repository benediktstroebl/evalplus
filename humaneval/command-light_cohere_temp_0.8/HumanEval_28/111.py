```python
from typing import List
def concatenate(strings: List[str]): 
    return ''.join(strings)

def test_concatenate():
    assert concatenate([]) == ''
    assert concatenate(['a']) == 'a'
    assert concatenate(['a', 'b']) == 'ab'
    assert concatenate(['a', 'b', 'c']) == 'abc'

print("Test successful")
```