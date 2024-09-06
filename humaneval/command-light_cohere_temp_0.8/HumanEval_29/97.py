```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    strings = ["abc", "bcd", "cde", "a", "array", "hello"]
    prefix = "a"

    result = filter_by_prefix(strings, prefix)
    assert result == ['abc', "array"], "Should be ['abc', 'array'], got: %s" % result

    strings = ["a", "ab"]
    result = filter_by_prefix(strings, prefix)
    assert result == [], "Should be empty, got: %s" % result

    strings = ["abc", "bcd"]
    result = filter_by_prefix(strings, "b")
    assert result == [], "Should be empty, got: %s" % result
```
The code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses the filter operation to return a new list that contains only the strings from the original list that start with the given prefix. The code also has a `test_filter_by_prefix` function that tests the `filter_by_prefix` function by passing different input strings and expected output.