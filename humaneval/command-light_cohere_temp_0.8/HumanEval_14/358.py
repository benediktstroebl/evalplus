```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + [string]

# Test cases
test_data = [
    "abc",
    "123",
    "",
    "!"
]

test_cases = [
    lambda s: all_prefixes(s) == test_data,
    lambda s: notmatch('^.*? in all_(? test_data)
]

def test_function(test_case):
    assert all_prefixes(test_case()) == test_data, "Test failed: {}".format()

test_cases()

``` 
This code defines a function all_prefixes that returns a list of all prefixes in the string, excluding an empty string. The test_cases define a set of test functions that pass or fail the all_prefixes function with a given string. The test_function contains the tests and is responsible for asserting the correctness of the all_prefixes function.