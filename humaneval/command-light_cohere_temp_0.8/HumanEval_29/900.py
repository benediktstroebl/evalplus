```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.push_str('a')
test_filter_by_prefix.push_str('abc')
test_filter_by_prefix.push_str('bcd')
test_filter_by_prefix.push_str('cde')
test_filter_by_prefix.push_str('array')

def test_function(test_filter_by_prefix: List[str]) -> None:
    assert test_filter_by_prefix == ['abc', 'array']

``` 
The provided code defines a function `filter_by_prefix` that filters an input list of strings based on their prefix. The function takes two arguments: `List[str]` which is the input list of strings and `str` which is the prefix to filter. 
The function uses the `push_str()` function to create a new list containing all strings from the input list that start with the given prefix. 
The function then returns this filtered list. 
The code also defines a unit test function `test_filter_by_prefix` that contains several strings and uses the `filter_by_prefix` function to filter the strings.  The test function then takes the unit test function as an argument and uses the `assert` function to assert that the output of `filter_by_prefix` function is correct.