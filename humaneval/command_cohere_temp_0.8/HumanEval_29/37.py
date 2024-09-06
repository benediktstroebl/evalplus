```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that begin with the input prefix. The function utilizes list comprehension, filtering out the strings from the input list that do not start with the input prefix.

To test it, you can use the following code:
```python
from pyutils import test

def test_list_with_prefix():
    assert filter_by_prefix(
        ["abc", "bcd", "cde", "array"], "a"
    ) == ["abc", "array"]

test(test_list_with_prefix)
```

The expected result of `filter_by_prefix(["abc", "bcd", "cde", "array"], "a")` is `["abc", "array"]`, as the input list contains two strings that start with the "a" prefix.