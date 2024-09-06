```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.push_one('abc')
test_filter_by_prefix.push_one('bcd')
test_filter_by_prefix.push_one('cde')
test_filter_by_prefix.push_one('array')
test_filter_by_prefix.push_one('ef')

def test():
    assert filter_by_prefix(test_strings, 'a') == ['abc']
    assert filter_by_prefix(test_strings, 'b') == ['bcd']
    assert filter_by_prefix(test_strings, 'c') == ['cde']
    assert filter_by_prefix(test_strings, 'array') == ['array']
    assert filter_by_prefix(test_strings, 'xx') == []

if __name__ == "__main__":
    test()
 ``` 
The code you provided is a Python script with a self-contained function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the test strings that start with the specified prefix, and returns a new list containing only those strings. The unit tests ensure the expected behavior of the function. The `test` function is used to run the tests.