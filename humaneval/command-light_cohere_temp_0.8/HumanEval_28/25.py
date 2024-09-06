```python
from typing import List
def concatenate(strings: List[str]):
    return ''.join() + ''.join(strings)

def test_concatenate():
    assert concatenate([]) == '', 'empty list should return empty string'
    assert concatenate(['a']) == 'a', 'single string should be returned'
    assert concatenate(['a', 'b', 'c']) == 'abc', 'should concatenate correctly'

if __name__ == "__main__":
    test_concatenate()
```