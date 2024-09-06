```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Test the function with empty list
test_concatenate():
    assert concatenate([]) == ''

# Test the function with list of strings
test_concatenate2():
    assert concatenate(['a', 'b', 'c']) == 'abc'

# Test the function with single string
test_concatenate3():
    assert concatenate('x') == 'x'
```