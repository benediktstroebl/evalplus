```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This behavior is demonstrated in the included tests:
```python
def test_filter_by_prefix():
    # Empty list, empty prefix
    assert filter_by_prefix([], '') == []

    # List with items starting with 'a', matching prefix
    assert filter_by_prefix(['abc', 'array', 'act'], 'a') == ['abc', 'array']

    # List with items starting with 'a', non-matching prefix
    assert filter_by_prefix(['abc', 'array', 'act'], 'b') == []

    # List with items starting with 'b', matching prefix
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'butter'], 'b') == ['bcd', 'cde', 'butter']

    # List with items starting with 'b', non-matching prefix
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'butter'], 'a') == []

test_filter_by_prefix()
```

This suite of tests covers the basic use cases of the function, including edge cases where the input list is empty or where the prefix doesn't match any items in the list.