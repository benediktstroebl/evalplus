```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Unit tests
strings = ["abc", "bcd", "cde", "array", "xx", "yy"]
prefix = "x"

test_strings = [("should start with 'x'",)

result = filter_by_prefix(strings, prefix)
should_be = [("x",)]

assert result == should_be
test_result = filter_by_prefix([strings[:2], prefix])
should_also = [("abc", "xx", "yy")]

assert test_result == should_also
```