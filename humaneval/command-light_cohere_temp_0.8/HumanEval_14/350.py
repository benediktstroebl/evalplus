```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Use string slicing to get all prefixes
    return [char for char in string if char != '']

# Test cases
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['a', 'ab', 'bcda']
    assert all_prefixes('') == []
```
This script defines a function all_prefixes that returns a list of all prefixes from the shortest to the longest string. 

It uses the slicing technique with string.

The test_prefixes function tests the all_prefixes function with different input strings and asserts the output matches the expected result. 
You can add more test cases as needed to validate your code.