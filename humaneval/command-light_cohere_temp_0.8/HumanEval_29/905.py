```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test case:
def test():
    strings = ['abc', 'bcd', 'cde', 'array', ' freedb']
    prefix = 'a'
    result = filter_by_prefix(strings, prefix)
    assert result == ['abc', 'array'], "Invalid result"


# Run the function and test it
test()
``` 
This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. 
The test case verifies that the function correctly filters the strings by passing the test data and checking if the result is as expected.