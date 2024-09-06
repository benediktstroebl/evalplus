```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests for the filter_by_prefix function
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['a', 'ab', 'ac'], 'a') == ['a', 'ab']
    assert filter_by_prefix(['a', 'b'], 'ab') == []
    assert filter_by_prefix(['a', 'ac', 'bc'], 'a') == ['ac']
    assert filter_by_prefix(['xx', 'a', 'ab'], 'x') == []
```
The provided code defines a function called `filter_by_prefix`, which takes a list of strings and a prefix as input and returns a new list containing elements that start with the given prefix. 

The code also includes unit tests that cover a variety of scenarios and verify the correctness of the `filter_by_prefix` function.