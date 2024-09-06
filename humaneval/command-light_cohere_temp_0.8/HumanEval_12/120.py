```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string.
    """
    string = strings[0]
    if len(string) < len(s):
        return s
    for s in strings:
        if len(s) > len(string):
            string = s
    return string
def test_longest() -> None:
    """Test longest function with a sample input."""
    assert longest(['a', 'bb', 'ccc']) == 3
    assert longest(['a', 'bc']) == 2
    assert longest([]) == 0
    assert longest(['aa', 'aa']) == 2
    assert longest(['aa', 'bb', 'aaa']) == 3
```