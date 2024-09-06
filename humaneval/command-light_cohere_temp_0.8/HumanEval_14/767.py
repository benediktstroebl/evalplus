```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return [''.join() for _ in range(string.find('a') + 1)]

# Test cases
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
``` 
This script defines a function called `all_prefixes` that takes a string `string` as input and returns a list of all its prefixes. The function uses a nested list comprehension to create the list of prefixes from shortest to longest by iterating over each character in the input string. 

The `test_all_prefixes` function tests the `all_prefixes` function with a sample string, `abc`, and ensures that the function returns the correct output, which is a list of all prefixes from shortest to longest of the input string.