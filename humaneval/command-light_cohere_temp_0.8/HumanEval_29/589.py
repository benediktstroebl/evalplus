```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Unit tests for the filter_by_prefix function
def test_filter_by_prefix():
    assert filter_by_prefix([], 'a') == ['a']
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert filter_by_prefix(['xxy', 'yyz', 'zba'], 'xy') == []
``` 
The code defines a function `filter_by_prefix` that takes in a list of strings and a prefix as input. The function then returns a list of strings in the input list that start with the given prefix.

The code also provides unit tests for the `filter_by_prefix` function using the `assert` statement, which checks that the function's output matches the expected output for the given input.