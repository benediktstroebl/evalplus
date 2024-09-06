```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests using only a sample input list and golden-copy expected output

test_data = [['abc', 'bcd', 'cde', 'array', 'hello']
test_case1 = ['a']
test_case2 = ['a', 'bc']
test_case3 = ['a', 'bcd', 'cd']
test_case4 = ['bcda', 'array', 'a']

def test_filter_by_prefix():
    actual_output = filter_by_prefix(test_data, 'a')
    assert actual_output == test_case1
    assert actual_output == test_case2
    assert actual_output == test_case3
    assert actual_output == test_case4

def test_filter_by_prefix_2():
    actual_output = filter_by_prefix(test_data, 'bcd')
    assert actual_output == test_case3
def test_filter_by_prefix_3():
    actual_output = filter_by_prefix(test_data, 'hello')
    assert actual_output == []
```
The code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a filtered list of strings that start with the given prefix. 

The code also includes unit tests using a test data set and asserts that the function's output matches the expected output for different input combinations.