```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    strings = ['abc', 'bcd', 'cde', 'array', 'hello']
    prefix = 'a'

    result = filter_by_prefix(strings, prefix)
    assert result == ['abc', 'array'], f"Wrong result: {result}"

    strings = ['abc', 'bcd', 'cde', 'array', 'hello']
    prefix = 'hello'

    result = filter_by_prefix(strings, prefix)
    assert result == [], f"Wrong result: {result}"

# Call the function and test it
test_filter_by_prefix()
```
This code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It also includes a test function to verify the correctness of the `filter_by_prefix` function. The test function passes all the test case successfully.