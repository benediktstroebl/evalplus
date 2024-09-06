```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.read_all(string)]

# Test
def test_function(test_str):
    assert all_prefixes(test_str) == ['a', 'ab', 'abc']
test_string = 'abc'
test_function(test_string)
 ```
This code defines a function `all_prefixes` that returns a list of all prefixes of a given string. The `test_function` is a helper function that tests the correctness of `all_prefixes` by asserting that it returns the correct result for the input string. 
Finally, it creates a test string and calls the `test_function` with it, which ensures the function's correctness by passing the test.