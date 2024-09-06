```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


def test_filter_by_prefix():
    strings = ['abc', 'bcd', 'cde', 'array', 'hello']
    prefix = 'a'
    expected = ['abc', 'array']
    actual = filter_by_prefix(strings, prefix)
    assert actual == expected, "Filtering failed"


# Run the tests
test_filter_by_prefix()
```
This Python script defines a function `filter_by_prefix` that filters a list of strings based on their prefix. The function takes in two arguments: a list of strings and a prefix to filter. The function then returns a list of strings that start with the given prefix. 

The script also provides a function `test_filter_by_prefix` which is a simple test for the `filter_by_prefix` function. The test passes the test and is good practice to write, as it can serve as a quick verification of the correctness of your function.