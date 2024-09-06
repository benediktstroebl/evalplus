```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Run tests on the function
test_str = ['abc', 'bcd', 'cde', 'a']
test_result = filter_by_prefix(test_str, 'a')
assert test_result == ['abc', 'a'], "Test failed: {}".format()

test_str = ['abc', 'bcd', 'cde', 'array', 'a']
test_result = filter_by_prefix(test_str, 'a')
assert test_result == ['abc', 'array'], "Test failed: {}".format()

test_str = ['a']
test_result = filter_by_prefix([ 'abc', 'bcd', 'cde', 'array'], 'a')
assert test_result == ['a'], "Test failed: {}".format()

```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. It then runs a test cases to ensure that the function is working correctly.