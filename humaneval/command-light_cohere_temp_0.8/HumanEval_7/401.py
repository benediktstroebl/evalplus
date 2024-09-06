Here's the code:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests
strings = ["abc", "bacd", "cde", "array", " welcome"]
substring = "a"

# Test case 1
test_case1 = filter_by_substring(strings, substring)
assert test_case1 == ['abc', 'bacd', "array"]

# Test case 2
test_case2 = filter_by_substring([ "foo", "bar" , "hello"], "o")
assert test_case2 == ["foo", "bar"]

# Test case 3
test_case3 = filter_case1(["welcome", "hello"])
assert test_case3 == ["hello", "welcome"]
```

Please note can help you with any other questions you might have.