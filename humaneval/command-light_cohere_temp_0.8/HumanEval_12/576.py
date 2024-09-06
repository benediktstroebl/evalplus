```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the length of the longest string.
    """
    return max(len(x) for x in strings)

# Unit tests
def test_longest():
    assert longest(['a', 'b', 'c']) == 3
    assert longest(['a', 'bb', 'ccc']) == 3
    assert longest([]) == 0
    assert longest(['a', 'ab', 'abc']) == 2
    assert longest(['a', 'aa', 'aaa']) == 3
```

The code defines a function `longest` that calculates the length of the longest string in a list, then tests its functionality with various input scenarios using the `test_longest` function.  This use of for the expected results.