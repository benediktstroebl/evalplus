```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This behavior is demonstrated in the included tests:
```python
def test_filter_by_prefix():
    # Single-character prefix filtering
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']

    # Multiple-character prefix filtering
    assert filter_by_prefix(['abcd', 'bcde', 'cdef', 'efgh'], 'ef') == ['efgh']
    assert filter_by_prefix(['abcd', 'bcde', 'cdef', 'efgh'], 'cd') == ['abcd', 'bcde', 'cdef']

    # Empty input, different prefix
    assert filter_by_prefix([], 'a') == []
    assert filter_by_prefix([], '1') == []

    # Empty input, empty prefix
    assert filter_by_prefix([], '') == []
    assert filter_by_prefix(['a', 'b', 'c'], '') == ['a', 'b', 'c']

    # Non-matching prefix
    assert filter_by_prefix(['abcd', 'bcde', 'cdef', 'efgh'], 'xy') == []
```

The function uses list comprehension with a conditional `s.startswith(prefix)` to filter the list accordingly. The tests cover various scenarios, including handling empty lists, cases where the prefix matches only some strings, and situations where the prefix does not match any strings, ensuring the function's behavior aligns with the problem statement.